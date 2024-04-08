from django.db import models
from django.contrib.auth.models import AbstractUser
# 기본 유저 클래스 --> 상속할거임 

# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100) 
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

    
