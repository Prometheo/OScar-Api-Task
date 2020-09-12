from rest_framework import generics
from ..serializers import login
from django.contrib.auth import get_user_model

#get the user model active in the project(Custom user model in this case)

User = get_user_model()

class CreateUser(generics.CreateAPIView):
    """
    An endpoint for creating users, email and password fields must be filled.
    """
    serializer_class = login.UserSerializer

class ListUsers(generics.ListAPIView):
    """
       Returns a List of all Users in the db, with details such as name, email and date joined.
    """
    queryset = User.objects.all()
    serializer_class = login.UserSerializer