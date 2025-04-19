from . models import Profile
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

def createProfile(sender, instance, created, *args, **kwargs):
    if created:
        created_user = instance
        Profile.objects.create(user = instance)



# @receiver(post_delete, sender = Profile)
def deleteUser(sender, instance, *args, **kwargs):
    instance.user.delete()    


post_delete.connect(deleteUser, sender=Profile)
post_save.connect(createProfile, sender=User)


