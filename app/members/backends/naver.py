import json

import requests
from django.contrib.auth import get_user_model

from config import settings

User = get_user_model()


class NaverBackend:

    def authenticate(self, code):
        HEADERS = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }

        def get_access_token(code):
            url = "https://nid.naver.com/oauth2.0/token"
            params = {
                'grant_type': 'authorization_code',
                'client_id': settings.NAVER_CLIENT_ID,
                'client_secret': settings.NAVER_SECRET_KEY,
                'code': code,
                'state': '200'
            }

            response = requests.post(url, params, headers=HEADERS)
            response_dict = response.json()
            access_token = response_dict['access_token']
            return access_token

        def get_user_info(access_token):

            url = " https://openapi.naver.com/v1/nid/me"
            HEADERS.update({'Authorization': "Bearer {}".format(access_token)})
            response = requests.post(url, headers=HEADERS)
            return response.json()

        def create_user_from_kakao_user_info(user_info):

            naver_id = user_info['id']
            email = user_info['email']

            user, __ = User.objects.get_or_create(
                username=naver_id,
                defaults={
                    'email': email,
                }
            )

            if __ is True:
                user.auth = 'N'
                user.save()
            return user

        access_token = get_access_token(code)
        user_info = get_user_info(access_token)
        user = create_user_from_kakao_user_info(user_info['response'])
        return user
