from django.urls import path
from .views.register import CreateUser
from oscarapi.urls import urlpatterns as og

urlpatterns = [
    path("register/", CreateUser.as_view(), name="create_user"),
] + og


