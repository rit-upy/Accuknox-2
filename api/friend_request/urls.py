from django.urls import path
from .views import FriendRequest, ListUsers, SearchAPIView, SendRequestView

urlpatterns = [
    path('send/', SendRequestView.as_view()),
    path('accept/<int:user>', FriendRequest.as_view({'put':'update'})),
    path('reject/<int:pk>', FriendRequest.as_view({'delete':'destroy'})),
    path('list/<str:status>/', ListUsers.as_view()), 
    path('search/', SearchAPIView.as_view())
]
