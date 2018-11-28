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
from django.urls import path, include

from .views import accounts_login, accounts_social_login

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    path('weapon/', include('weapon.urls')),
    path('armor/', include('armor.urls')),
    path('members/', include('members.urls')),
    # 기본적으로 login page가 지원되며 따로 custom하여 사용할 수 있다.
    # path('accounts/login/', accounts_login.account_login, name='accounts_login'),
    path('accounts/', include('allauth.urls')),
    path('index/', accounts_social_login.SocialLogin.as_view(), name='index'),
]
