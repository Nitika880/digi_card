"""cardrest1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from app1 import views
from app1.views import PersonalCardView, QRCodeAPIView, GetUserProfileView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
path('register/', views.RegisterView.as_view()),
    path('gettoken/', TokenObtainPairView.as_view(), name='gettoken'),
    path('refreshtoken', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken', TokenVerifyView.as_view(), name='token_verify'),
    path('personal/',PersonalCardView.as_view(),name='personal'),
    path('add_data/', QRCodeAPIView.as_view(), name='Create Data And Get QR'),

    path('get_user/<user_key>/', GetUserProfileView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


