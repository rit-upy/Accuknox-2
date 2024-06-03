
from rest_framework import generics,status, views
from .models import Friends
from authentication.models import User
from .serializers import AcceptedUsersSerializer,SearchUsersSerializer,RequestSerializer
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.utils.functional import cached_property

# Create your views here.
class ListUsers(generics.ListAPIView):
    queryset = Friends.objects.all()
    serializer_class = AcceptedUsersSerializer
       
    @cached_property #caching as it is being called twice. Once in self.list and the other in renderers.py (get_filter_form)
    def get_queryset(self):
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
        return Friends.objects.filter(pending = pending)


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

class FriendRequest(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = RequestSerializer
    
    
    def destroy(self, request, *args, **kwargs):
        friend = self.get_object()
        if friend.pending is False:
            raise ValidationError('Request is already accepted and hence can\'t be deleted')

        return super().destroy(request, *args, **kwargs)
    
