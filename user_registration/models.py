from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
#create a custom user model, so we can use email as verification instead of username
class User(AbstractUser):
   email = models.EmailField(_('email address'), unique=True)
   username= None
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['first_name','last_name']

   def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
