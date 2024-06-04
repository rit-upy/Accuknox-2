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
        fields = ('email', 'full_name')

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        exclude = ('pending',)

    def create(self, validated_data): #creating only one record for the friendship table
        user = validated_data['user']
        friend = validated_data['friend']
        # Check for duplicate friend request
        if Friends.objects.filter(user=user, friend=friend, pending=True).exists():
            raise ValidationError('Duplicate send friend request')

        # Check if a reverse request already exists
        if Friends.objects.filter(user=friend, friend=user, pending=True).exists():
            raise ValidationError('Friend request already received from this user')

        # Create the friend request
        validated_data['pending'] = True
        return super().create(validated_data) 


    def update(self, instance, validated_data): #accept friend request
        print('The serializer for accepting the friend request is being called')
        user = validated_data['user']
        friend = validated_data['friend']

        #check for whether user exists in table
        user_friend_exists = Friends.objects.filter(user = user, friend = friend, pending = True)
        reverse_user_friend_exists = Friends.objects.filter(user = friend, friend = user, pending = True)
        if not user_friend_exists.union(reverse_user_friend_exists).exists():
            raise ValidationError('You must send a friend request before it can be accepted')
        
        #check for duplicate friend request
        user_friend_check_accept = Friends.objects.filter(user = user , friend = friend, pending = False)
        reverse_user_friend_check_accept = Friends.objects.filter(user = friend, friend = user, pending = False)
        if user_friend_check_accept.union(reverse_user_friend_check_accept).exists():
            raise ValidationError('Duplicate accept friend request')
        
        validated_data['pending'] = False
        return super().update(instance, validated_data)
    

    
