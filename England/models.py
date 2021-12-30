from django.db import models
from django.urls import reverse
from django.conf import settings
#from django.contrib.auth.models import User
# Create your models here.


User = settings.AUTH_USER_MODEL



class Groupss(models.Model):
    name = models.CharField(null=True,max_length=200)
    users = models.ManyToManyField(to=User,related_name='users')
    grouphead = models.OneToOneField(User,null = True,on_delete = models.CASCADE,default=True,related_name='grouphead')

    def __str__(self):
        return str(self.name)

    def change_groupname(self,usernamee):
        p_user = User.objects.get(username=usernamee)

        if self.grouphead == p_user:
            print('sgg')
            return True
        print('not a group head')
        return False

class Chatmessage(models.Model):
    chat_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='chat_user')
    chat = models.ForeignKey(Groupss,null=True,on_delete=models.CASCADE,related_name='messages')
    message = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.chat.name} by {self.chat_user}'
