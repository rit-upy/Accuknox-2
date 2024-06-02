from django.urls import path
from .views import SendFriendRequest, AcceptFriendRequest,RejectFriendRequest

urlpatterns = [
    path('send/', SendFriendRequest.as_view() ),
    path('accept/<int:pk>', AcceptFriendRequest.as_view()),
    path('reject/<int:pk>', RejectFriendRequest.as_view())
]
