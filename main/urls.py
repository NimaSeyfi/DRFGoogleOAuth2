from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views
from main.OAuth import urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = DefaultRouter()
router.register('GoogleAccounts', views.GoogleAccountViewSet)
router.register('scripts', views.ScriptViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('oauth/', include(urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView .as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
