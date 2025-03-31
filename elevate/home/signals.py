from django.db.models.signals import post_save, post_delete
from . models import Profile
from django.contrib.auth.models import User


def createProfile(sender, instance, created, *args, **kwargs):
    if created:
        created_user = instance
        Profile.objects.create(
            user = created_user
        )


def deleteUser(sender, instance, *args, **kwargs):
    instance.user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)




