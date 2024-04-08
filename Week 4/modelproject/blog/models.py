from django.db import models # models이라는 모듈(라이브러리) 불러오기 
from accounts.models import CustomUser
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100) # 문자열을 담는 필드
    body = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
