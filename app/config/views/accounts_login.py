from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from ..forms import LoginForm


def account_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('index')

        else:
            return HttpResponse('로그인 실패')

    else:
        context = {
            'login_form': LoginForm(),
        }

    return render(request, 'account_app/nibit_login.html', context)
