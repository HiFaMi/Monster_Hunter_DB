from django.urls import path

from .views import *

app_name = 'user'

urlpatterns = [
    path('kakao_oauth/', kakao_auth.KakaoAuth.as_view(), name='kakao_auth'),
    path('naver_oauth/', naver_auth.NaverAuth.as_view(), name='naver_auth'),
]
