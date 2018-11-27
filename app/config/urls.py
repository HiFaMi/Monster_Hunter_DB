"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from members.views import accounts_login, accounts_social_login
from .views import index, account

# admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    path('weapon/', include('weapon.urls')),
    path('armor/', include('armor.urls')),
    path('members/', include('members.urls')),
    path('accounts/login/', accounts_login.account_login, name='accounts_login'),
    path('accounts/', include('allauth.urls')),
    path('index/', accounts_social_login.SocialLogin.as_view(), name='index'),
]
