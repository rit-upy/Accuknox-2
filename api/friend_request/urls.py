from django.urls import path
from .views import FriendRequest, ListUsers

urlpatterns = [
    path('send/', FriendRequest.as_view({'post':'create'})),
    path('accept/<int:pk>', FriendRequest.as_view({'put':'update'})),
    path('reject/<int:pk>', FriendRequest.as_view({'delete':'destroy'})),
    path('list/<str:status>', ListUsers.as_view())
]
