
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE ,null=True, blank=True)
    name = models.CharField(max_length=50)
    # roll = models.CharField(max_length=50,default=1) user's username is roll
    
    def __str__(self):
        return self.name
        
"""@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.user = User
    instance.profile.save() """
