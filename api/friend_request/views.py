
from rest_framework import generics,status
from .models import Friends
from authentication.models import User
from .serializers import AcceptedUsersSerializer,SearchUsersSerializer, SendRequestSerializer,AcceptRequestSerializer, RejectRequestSerializer
from rest_framework.response import Response
from django.core.exceptions import ValidationError

# Create your views here.
class BaseFriendsListView(generics.ListAPIView):
    queryset = Friends.objects.all()
    serializer_class = AcceptedUsersSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if hasattr(self, 'pending_status'):
            queryset = queryset.filter(pending=self.pending_status)
        return queryset

class ListAcceptedUsers(BaseFriendsListView):
    pending_status = False

class ListPendingUsers(BaseFriendsListView):
    pending_status = True

class SearchAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = SearchUsersSerializer
    def get_queryset(self):
        search_email = self.request.query_params.get('email', None)

        if search_email is not None:
            return User.objects.filter(email=search_email).\
                values('email', 'full_name').first()

        else:
            name = self.request.query_params.get('name', None)
        if name is not None:
            return User.objects.filter(name__icontains = name)  
        return Response('Please enter the email or the name field.',\
                             status=status.HTTP_400_BAD_REQUEST)

class SendFriendRequest(generics.CreateAPIView):
    queryset = Friends.objects.all()
    serializer_class = SendRequestSerializer

class AcceptFriendRequest(generics.UpdateAPIView):
    queryset = Friends.objects.all()
    serializer_class = AcceptRequestSerializer
    
    
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    

class RejectFriendRequest(generics.DestroyAPIView):
    queryset = Friends.objects.all()
    serializer_class = RejectRequestSerializer

    def destroy(self, request, *args, **kwargs):
        friend = self.get_object()
        print(friend)
        if friend.pending is False:
            raise ValidationError('Request is already accepted')

        return super().destroy(request, *args, **kwargs)
    