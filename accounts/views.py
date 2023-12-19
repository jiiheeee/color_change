from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer

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
    def post(self, request):
        user_id = request.data.get("id")
        password = request.data.get("password")
        try:
            login_data = User.objects.get(email=user_id, password=password)
            serializer = UserSerializer(login_data)
        except Exception as e:
            return HttpResponse('아이디 및 비밀번호를 확인해주세요.', status=400)
        return Response(serializer.data, status=200)