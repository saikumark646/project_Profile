# imports from rest_framework and django
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User


#imports from user_app
from user_app.serializers import Profileserializer
from user_app.models import Profile
from user_app.utils import validate_email_address,IsUserAuthOrSameUser

# Create your views here.


class CreateUser(generics.ListCreateAPIView):

    """
        Created-by: sai
        required params: first_name, password, email
        response: response is a dict containing the message and status code

    """
    serializer_class = Profileserializer
    permission_classes = [IsAuthenticated]

    def create(self, request,*args, **kwargs):
        try:
            first_name  =request.data.get('first_name')
            last_name  =request.data.get('last_name','')
            password = request.data.get('password')
            email = request.data.get('email')
            required_fields = ['first_name', "password", 'email']

            for i in required_fields:
                if i not in request.data:
                    response  = { "status_code": 400,"message": f"{i} is required field",}
                    return Response(
                        response,status=status.HTTP_400_BAD_REQUEST
                    )
            
            validated_email  = validate_email_address(email)
            query  = User.objects.filter(email=email)

            if query.exists():
                response  = { "status_code": 400,"message": f"{first_name} account is already created",}
                return Response(
                    response,status=status.HTTP_400_BAD_REQUEST
                )
            user = User.objects.create(username=first_name)
            user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            data = {}
            data['user'] = user.id
            if first_name:
                data['first_name'] = first_name
            if last_name:
                data['last_name'] = last_name

            serializer  = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            response  = { "status_code": 200,"message": f"{first_name} account created successfully"}   
            return Response(
                    response,status=status.HTTP_201_CREATED
            )
        except Exception as e:
            response = {
                'status_code': 400,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class UpdateProfile(viewsets.ModelViewSet):
    queryset  = Profile.objects.all()
    serializer_class = Profileserializer
    permission_classes = [IsUserAuthOrSameUser]
    http_method_names = ['get','patch','delete']

            