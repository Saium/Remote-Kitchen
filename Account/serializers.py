from rest_framework import serializers
from .models import CustomUser


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_owner', 'is_employee']

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'is_owner', 'is_employee']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            is_owner=validated_data.get('is_owner', False),
            is_employee=validated_data.get('is_employee', False),
        )
        return user