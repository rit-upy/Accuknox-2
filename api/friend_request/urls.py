from django.urls import path
from .views import SendFriendRequest

urlpatterns = [
    path('send/', SendFriendRequest.as_view() )
]
