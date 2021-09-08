from django.contrib import admin
from main.OAuth import oauthModels
from django.contrib.auth import get_user_model
from main import models


User = get_user_model()

admin.site.register(User)
admin.site.register(oauthModels.AccessKey)
admin.site.register(oauthModels.BlockedAccessKey)
admin.site.register(models.Script)
