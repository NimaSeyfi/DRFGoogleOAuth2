import requests
import json
from django.shortcuts import redirect
from urllib.parse import urlencode
from rest_framework.decorators import api_view
from . import serializers
from . import oauthModels
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import AnonymousUser
from main import models
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings


# @api_view(['POST'])
@api_view()
def oauth_callback_handler(request):
    # if request.method == 'POST':
    authorization_code = request.GET.get('code')
    print(authorization_code)
    access_token = get_access_token(authorization_code)
    access_key_serializer = serializers.AccessKeySerializer(data=access_token)
    access_key_serializer.is_valid()
    access_key_instance = access_key_serializer.save()
    user_instance = update_user_access_key(request, access_key_instance)
    #user_token = get_tokens_for_user(user_instance)
    # print(jwt.decode(user_token, settings.SIMPLE_JWT['SECRET_KEY'], algorithms=["HS256"]))
    #login_user(user_instance, user_token)
    #redirect("http://127.0.0.1:8000")
    #return Response(data=user_token)
    return redirect("http://127.0.0.1:8000/api/")

def update_user_access_key(request, access_key_instance):
    google_data = get_google_profile(access_token=access_key_instance)
    name = google_data.get('given_name')
    user = request.user
    print(google_data)
    print(type(user))
    if models.User.objects.filter(username__exact=name).exists():
        user_instance = models.User.objects.get(username=name)
    else:
        user_instance = models.User.objects.create_user(username=name)
    if user_instance.access_key:
        last_access_key = user_instance.access_key
        last_access_key.delete()
    user_instance.access_key = access_key_instance
    user_instance.save()
    return user_instance


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def login_user(user, token):
    pass

def get_google_profile(access_token):
    data_url = "https://www.googleapis.com/oauth2/v1/userinfo?alt=json"
    header_dict = {"Authorization": "Bearer %s" % access_token.access_token}
    print(header_dict)
    req = requests.get(data_url, headers=header_dict)
    google_user_data = json.loads(req.content.decode('utf-8'))
    return google_user_data


# @api_view(['POST'])
@api_view()
def get_authorization_code(request):
    # if request.method == 'POST':
    client_id = "718733559132-utomvqhli5k31kei2ocij8i2emoci9jl.apps.googleusercontent.com"
    redirect_uri = "http://127.0.0.1:8000/oauth/ruri"
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": "https://www.googleapis.com/auth/userinfo.profile"
    }
    google_oauth_url = "https://accounts.google.com/o/oauth2/v2/auth?" + urlencode(params)
    return redirect(google_oauth_url)


def get_access_token(authorization_code):
    client_id = "718733559132-utomvqhli5k31kei2ocij8i2emoci9jl.apps.googleusercontent.com"
    client_secret = "vWzaDiW58ljhs_4Ve8XhY6FL"
    redirect_uri = "http://127.0.0.1:8000/oauth/ruri"
    url = "https://oauth2.googleapis.com/token"
    params = {
        'code': authorization_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    response = requests.post(url, data=params)
    res = json.loads(response.content.decode('utf-8'))
    return res


@api_view(['POST'])
def revoke_token(request, token, ip):
    if request.method == 'POST':
        access_token = get_object_or_404(oauthModels.AccessKey, pk=token.id)
        data = get_access_key_data(token, ip)
        blocked_serializer = serializers.BlockedAccessKeySerializer(data=data)
        if blocked_serializer.is_valid():
            blocked_serializer.save()
            return Response(blocked_serializer.data)
        else:
            return Response(blocked_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_access_key_data(access_token, ip):
    data = {
        'access_token': access_token.access_token,
        'expires_in': access_token.expires_in,
        'token_type': access_token.token_type,
        'scope': access_token.scope,
        'id_token': access_token.id_token,
        'ip': ip
    }
    return data
