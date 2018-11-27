from django.urls import path, include

from .views import *

app_name = 'user'

urlpatterns = [

    path('kakao_oauth/', kakao_auth.KakaoAuth.as_view(), name='kakao_auth'),
    path('naver_oauth/', naver_auth.NaverAuth.as_view(), name='naver_auth'),
    path('local_oauth/', auth.UserAuth.as_view(), name='local_auth'),
    path('signup/', signup.UserSignup.as_view(), name='signup'),


]
