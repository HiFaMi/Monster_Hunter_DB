from django.shortcuts import render

from config import settings


def index(request):
    kakao_api = settings.KAKAO_APP_ID
    naver_api = settings.NAVER_CLIENT_ID

    context = {
        'kakao_api': kakao_api,
        'naver_api': naver_api,

    }

    return render(request, 'main.html', context)
