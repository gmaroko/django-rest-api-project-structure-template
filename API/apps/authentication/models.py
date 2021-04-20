from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import EmailValidator, validate_email

# admins
# staff
# guest

class Applicant(models.Model):
    username = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50,validators=[EmailValidator, validate_email],default="marokogideon@gmail.com")
    password = models.CharField(max_length=16, null=False,default="password2011")