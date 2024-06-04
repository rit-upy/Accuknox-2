from django.urls import path
from .views import FriendRequest, ListUsers, SearchAPIView

urlpatterns = [
    path('send/', FriendRequest.as_view({'post':'create'})),
    path('accept/<int:pk>/<int:user>', FriendRequest.as_view({'put':'update'})),
    path('accept/<int:pk>/<int:user>', FriendRequest.as_view({'delete':'destroy'})),
    path('list/<int:pk>/<str:status>/', ListUsers.as_view()), 
    path('search/', SearchAPIView.as_view())
]
