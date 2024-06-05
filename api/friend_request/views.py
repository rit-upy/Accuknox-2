
from rest_framework import generics,status, views
from .models import Friends
from authentication.models import User
from .serializers import AcceptedUsersSerializer,SearchUsersSerializer,RequestSerializer, SendRequestSerializer
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from django.db.models import Q
from rest_framework import throttling
from pprint import pprint


# Create your views here.
class ListUsers(generics.ListAPIView):
    
    serializer_class = AcceptedUsersSerializer

    def get(self, request, *args, **kwargs):
        print(kwargs)
        user = kwargs.get('pk')
        status = kwargs.get('status')        

        if not user:
            raise ValidationError('User not provided')
        
        if not status:
            raise ValidationError('Status not provided')
        elif status.lower() == 'accepted':
            pending = False
        elif status.lower() == 'pending':
            pending = True
        else:
            raise ValidationError('Wrong status request!')
        
        friends = Friends.objects.filter(user__pk = user, pending = pending )
        reverse_friends = Friends.objects.filter(friend__pk = user, pending = pending)
        self.queryset = friends.union(reverse_friends)
        print(self.get_object())
        return super().get(request, *args, **kwargs)
       
    # @cached_property #caching as it is being called twice. Once in self.list and the other in renderers.py (get_filter_form)
    def get_queryset(self):
        # print(self.get_object())
        status = self.kwargs.get('status', None)
        print(f'status is {status.lower()}')
        if status is None:
            raise ValidationError('Argument not provided!')
        elif status.lower() == 'accepted':
            pending = False
        elif status.lower() == 'pending':
            pending = True
        else:
            raise ValidationError('Wrong status request!')
        # Friends.objects.filter(user = )
        return Friends.objects.filter(pending = pending)


class SearchAPIView(generics.ListAPIView):
    serializer_class = SearchUsersSerializer
    
    def get_queryset(self):
        search_email = self.request.query_params.get('email', None)

        if search_email is not None:
            return User.objects.filter(email=search_email)
        
        name = self.request.query_params.get('name', None)
        
        if name is not None:
            
            return User.objects.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        return Response('Please enter the email or the name field.',\
                             status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # if not queryset.exists():
        #     return Response('Please enter the email or the name field.', status=status.HTTP_400_BAD_REQUEST)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class FriendRequestThrottle(throttling.SimpleRateThrottle):
    scope = 'friend_request'
    rate = '3/minute'
    def get_cache_key(self, request, view):
        # Use the user's ID as part of the cache key to distinguish requests from different users
        user_id = request.user.id if request.user else None
        return f'{self.scope}-{user_id}'

    def allow_request(self, request, view):
        # Get the cache key for the current request
        cache_key = self.get_cache_key(request, view)
        # Get the number of requests made by the user within the throttle time window
        num_requests = self.cache.get(cache_key, 0)
        # Check if the user has exceeded the allowed number of requests
        if num_requests >= 3:
            return False
        # Increment the number of requests made by the user
        self.cache.set(cache_key, num_requests + 1, self.duration)
        return True


class FriendRequest(viewsets.ModelViewSet):
    
    serializer_class = RequestSerializer

    def get_throttles(self):
        if self.action == 'create':
            return [FriendRequestThrottle()]
        return super().get_throttles()

    def destroy(self, request, *args, **kwargs): #reject
        user = request.user
        friend_id = kwargs.get('pk')
        print(user.id,friend_id)
        if user.id == friend_id:
            return Response('User and friend are the same', status=status.HTTP_400_BAD_REQUEST)

        try:
            friend = Friends.objects.get(user = user, id = friend_id)
        except Friends.DoesNotExist:
            return Response('You are not friends with this person', status=status.HTTP_400_BAD_REQUEST)
        
        if friend.pending is False:
            return Response('Request is already accepted and can\'t be deleted', status=status.HTTP_400_BAD_REQUEST)
        
        friend.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SendRequestView(generics.CreateAPIView):
    serializer_class = SendRequestSerializer
    