from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User

class SignUpView(APIView):
    def post(self, request):
        user_name = request.data.get("name")
        mail = request.data.get("mail")
        password = request.data.get("password")

        User.objects.create(
            name=user_name,
            mail=mail,
            password=password
        )
        return HttpResponse('회원가입이 완료되었습니다.')