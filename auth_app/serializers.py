from .models import UserPanel, Users
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Users
        fields = '__all__'

class PanelSerializer(serializers.ModelSerializer) :
    class Meta:
        model = UserPanel
        fields = '__all__'
