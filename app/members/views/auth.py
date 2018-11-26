from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, render
from rest_framework.views import APIView

from ..serializers.auth import UserAuthSerializer

User = get_user_model()


class UserAuth(APIView):

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        login(user)
        return render(request, 'test_account.html')
