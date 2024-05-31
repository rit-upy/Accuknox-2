from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import UserModel
class LoginSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    password = serializers.CharField()

    def is_valid(self, *, raise_exception=False):
        super().is_valid(raise_exception=raise_exception)
        



class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = 'last_login',

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)