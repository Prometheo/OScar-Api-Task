from rest_framework import serializers
from oscarapi.serializers import login
from django.contrib.auth import authenticate, get_user_model

#get the user model active in the project(Custom user model in this case)
User = get_user_model()

class UserSerializer(login.UserSerializer):
    class Meta:
        model= User
        fields = ('first_name', 'last_name', 'email', 'password', 'date_joined')
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined':{'read_only': True},
            }

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

#override the Login serializer so that users can login with email instead of username
class LoginSerializer(login.LoginSerializer):
    username= None
    email = serializers.CharField(max_length=50, required=True)

    def validate(self, attrs):
        user = authenticate(username=attrs["email"], password=attrs["password"])
        if user is None:
            raise serializers.ValidationError("invalid login")
        elif not user.is_active:
            raise serializers.ValidationError("Can not log in as inactive user")

        # set instance to the user so we can use this in the view
        self.instance = user
        return attrs