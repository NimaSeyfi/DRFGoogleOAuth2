from django.urls import path
from main.OAuth import views

urlpatterns = [path('', views.get_authorization_code),
               path('ruri', views.oauth_callback_handler),
               path('revoke', views.revoke_token)
               ]
