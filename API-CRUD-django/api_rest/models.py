from django.db import models

# Create your models here.

class User(models.Model):
    nickname = models.CharField(max_length=80, primary_key=True, default='NoNickname')
    name = models.CharField(max_length=120, default='NoName')
    email = models.EmailField(default='noemail@email.com')
    age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.nickname} | Email: {self.email}'
    