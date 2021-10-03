from django.db.models.signals import post_save, post_delete
# Create your models here.
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


# @receiver(post_save, sender=Profile)
# creating profile when user is created
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        # instance is the user info
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


# deleting user when profile is deleted
# deleting profile when user is deleted is done by models.cascade
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    # instance.user is the Profile.user info
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
