from rest_framework import views,generics,status
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from .serializers import LoginSerializer, SignUpSerializer
from .models import UserModel
# Create your views here.
class SignupAPIView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    queryset = UserModel.objects.all()


class LoginAPIView(views.APIView):
    
    serializer_class = LoginSerializer
    
    def post(self,request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_email = serializer.validated_data['user_email']
        password = serializer.validated_data['password']
        
        try:
            user = UserModel.objects.get(user_email__iexact = user_email)
  
        except:
            return Response('User Email not found', status = status.HTTP_401_UNAUTHORIZED)
        
        
        if not user.check_password(password):
            return Response('Wrong password!!', status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_200_OK)


