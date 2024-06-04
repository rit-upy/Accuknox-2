from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User
from django.core.exceptions import ValidationError
class LoginSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    password = serializers.CharField(write_only = True)



class SignUpSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    class Meta:
        model = User
        exclude = ('last_login',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        print('I am in the authentication signup create method')
        email = validated_data['email'].lower()
        validated_data['email'] = email
        validated_data['password'] = make_password(validated_data['password'])
        print('I am leaving the method')
        return super().create(validated_data)