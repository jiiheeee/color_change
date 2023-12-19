from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer
from django.contrib.auth import authenticate

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

class LogInView(APIView):
    def auth(self, user_id: str, password: str):
        # user_id, password 맞나?
        try:
            user = User.objects.get(mail=user_id, password=password)
        except User.DoesNotExist:
            return None
        return user

    def post(self, request):
        x = request.data
        user_id = request.data.get("user_id")
        password = request.data.get("password")

        user = self.auth(user_id, password)
        if user is not None:
            login_data = User.objects.get(mail=user_id, password=password)
            serializer = UserSerializer(login_data)
            return Response(serializer.data, status=200)
        else:
            return HttpResponse('아이디 및 비밀번호를 확인해주세요.', status=400)