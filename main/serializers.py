from rest_framework import serializers
from main import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')


class GoogleAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GoogleAccount
        fields = ()


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Script
        fields = ('id', 'context', 'language')
