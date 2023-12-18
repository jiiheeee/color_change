from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User

class UserDetailView(APIView):
    def get(self, request, user_id: int):
        user_detail = User.objects.get(id=user_id)
        pass
        # serializer