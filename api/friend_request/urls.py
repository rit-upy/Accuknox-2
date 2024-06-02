from django.urls import path
from .views import SendFriendRequest, AcceptFriendRequest

urlpatterns = [
    path('send/', SendFriendRequest.as_view() ),
    path('accept/<int:pk>', AcceptFriendRequest.as_view())
]
