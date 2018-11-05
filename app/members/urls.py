from django.urls import path

from .views import *

app_name = 'user'

urlpatterns = [
    path('oauth/', kakao_auth.KakaoAuth.as_view(), name='kakao_auth'),
]
