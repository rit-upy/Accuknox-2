from rest_framework import serializers
from .models import Friends, User

class AcceptedUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        exclude = 'pending',

class SearchUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        exclude = 'pending',

    def create(self,validated_data):
        validated_data['pending'] = True
        return super().create(validated_data)