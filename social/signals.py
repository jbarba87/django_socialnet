from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

#def create_post(sender, instance, created, **kwargs):
#  if created:
#)    print("\t Se acaba de creat un post")

#post_save.connect(create_profile, sender=User)
#post_save.connect(create_post, sender=Post)