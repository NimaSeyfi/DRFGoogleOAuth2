from rest_framework import serializers
from . import oauthModels

class AccessKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = oauthModels.AccessKey
        fields = ('access_token', 'expires_in', 'token_type', 'scope', 'id_token')

    def create(self, validated_data):
        return oauthModels.AccessKey.objects.create(**validated_data)

class BlockedAccessKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = oauthModels.BlockedAccessKey
        fields = ('ip', 'access_token', 'expires_in', 'token_type', 'scope', 'id_token')

    def create(self, validated_data):
        return oauthModels.BlockedAccessKey.objects.create(**validated_data)