from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from .serializers import UserSerializer

class UserDetailView(APIView):
    def get(self, request, user_id: int):
        user_detail = User.objects.get(id=user_id)
        serializer = UserSerializer(user_detail)
        return Response(serializer.data)
    
class LogInView(APIView):
    def post(self, request):
        user_id = request.data.get("id")
        password = request.data.get("password")
        try:
            login_data = User.objects.get(email=user_id, password=password)
        except Exception as e:
            return HttpResponse('아이디 및 비밀번호를 확인해주세요.')
        return Response()