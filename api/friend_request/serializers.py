from rest_framework import serializers
from .models import Friends, User
from django.core.exceptions import ValidationError

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
        exclude = ('pending',)

    def create(self,validated_data):
        if Friends.objects.filter(friend__email = validated_data['friend'], pending = True).exists():
            raise ValidationError('Duplicate send friend request')
        validated_data['pending'] = True
        return super().create(validated_data)

class AcceptRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        exclude = ('pending',)

    def update(self, instance, validated_data):
        print('The serializer for accepting the friend request is being called')
        if Friends.objects.filter(friend__email = validated_data['friend'], pending = False).exists():
            raise ValidationError('Duplicate accept friend request')
        validated_data['pending'] = False
        return super().update(instance, validated_data)    
    
    
