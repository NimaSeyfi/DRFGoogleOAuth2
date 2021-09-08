from main import serializers, models
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class GoogleAccountViewSet(viewsets.ModelViewSet):
    queryset = models.GoogleAccount.objects.all()
    serializer_class = serializers.GoogleAccountSerializer


class ScriptViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Script.objects.all()
    serializer_class = serializers.ScriptSerializer
