from django.urls import path
from .views import FriendRequest

urlpatterns = [
    path('send/', FriendRequest.as_view({'post':'create'})),
    path('accept/<int:pk>', FriendRequest.as_view({'put':'update'})),
    path('reject/<int:pk>', FriendRequest.as_view({'delete':'destroy'}))
]
