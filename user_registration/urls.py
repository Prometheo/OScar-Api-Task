from django.urls import path
from .custom_endpoint.views.register import CreateUser, ListUsers
from oscarapi.urls import urlpatterns as og

urlpatterns = [
    path("register/", CreateUser.as_view(), name="create_user"),
    path("users/", ListUsers.as_view(), name="list_users"),
] + og


