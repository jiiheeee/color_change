from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    mail = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    mixed_color_number = serializers.IntegerField(required=True)
    is_active = serializers.CharField(required=True)
    create_at = serializers.DateTimeField(required=True)
    update_at = serializers.DateTimeField(required=True)

    class Meta:
        model = User
        fields =(
            'name',
            'mail',
            'password',
            'mixed_color_number',
            'is_active',
            'create_at',
            'update_at'
        )