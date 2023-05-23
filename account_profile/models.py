from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, default="", blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Transaction(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    detail = models.TextField()
    success = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """This method create an associated profile when a user is created"""

    if created:
        Profile.objects.create(instance)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, **kwargs):
    instance.profile.save()
