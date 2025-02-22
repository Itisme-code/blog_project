from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    class StatusEnum (models.TextChoices):
        ACTIVE = 'active'
        BLOCKED = 'blocked'

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField(blank=True,null=True) 
    bio = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='profil_images/',blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    status = models.CharField(max_length=7,choices=StatusEnum.choices,default=StatusEnum.ACTIVE)
    subscribers = models.ManyToManyField('Profile',blank=True,related_name='subscribed_users')
    block_users = models.ManyToManyField('Profile',blank=True,related_name='blocked_users')

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return ''

    def __str__(self):
        return f"{self.user.get_full_name()}"
    
    def add_subscribe(self,profile):
        if not profile in self.subscribers.all():
            self.subscribers.add(profile)
            return True
        else:
            self.subscribers.remove(profile)
            return False
