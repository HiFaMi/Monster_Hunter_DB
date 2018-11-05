from django.shortcuts import render

from config import settings


def index(request):
    kakao_api = settings.KAKAO_APP_ID

    context = {
        'kakao_api': kakao_api,

    }

    return render(request, 'main.html', context)
