from django.shortcuts import render
from django.views.generic import TemplateView


class SocialLogin(TemplateView):
    template_name = 'accounts_app/test_account.html'
