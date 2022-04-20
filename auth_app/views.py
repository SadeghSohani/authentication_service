from email import message
from hashlib import sha256

from django.shortcuts import render
from .serializers import UserSerializer, PanelSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Users, UserPanel

class UserViewSet(viewsets.ViewSet) :

    def list(self, request) :
        users = Users.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    def create(self, request) :
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        username = request.data.get("username")
        password = request.data.get("password")
        token = sha256(f'{username} {password}'.encode()).hexdigest()
        message_response = {
            'user' : serializer.data,
            'token' : token
        }
        return Response(message_response, status=status.HTTP_201_CREATED)

    def authenticate_user(self, request) :
        username = request.headers.get("username")
        token = request.headers.get("token")
        print(username)
        print(token)
        user = Users.objects.raw(f'SELECT * FROM auth_app_users WHERE `username` = "{username}"')
        if sha256(f'{user[0].username} {user[0].password}'.encode()).hexdigest() == token :
            return Response({"message" : "tocken is valid.", "isvalid" : 1})
        else :
            return Response({"message" : "tocken is invalid.", "isvalid" : 0})

    def reserve_flight(self, request) :
        serializer = PanelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    def user_panel(self, request) :
        username = request.headers.get("username")
        token = request.headers.get("token")
        user = Users.objects.raw(f'SELECT * FROM auth_app_users WHERE `username` = "{username}"')
        if sha256(f'{user[0].username} {user[0].password}'.encode()).hexdigest() == token :
            panel_data = UserPanel.objects.raw(f"SELECT * FROM `auth_app_userpanel` WHERE `username` = '{username}'")
            serializer = PanelSerializer(panel_data, many=True)
            return Response(serializer.data)
        else :
            return Response({"message" : "tocken is invalid.", "isvalid" : 0})