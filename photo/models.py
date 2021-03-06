from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tag(models.Model):
    tag = models.CharField(blank=True, max_length=240)
    value = models.CharField(blank=True, max_length=240)


class Photo(models.Model):
    file = models.ImageField()
    # tags = models.ManyToManyField(Tag, through='Associate', related_name='tags')
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    name = models.CharField(blank=True, max_length=240, default='test')
    is_checked = models.BooleanField(default='False')

@receiver(post_save, sender=Photo)
def create_default_name(sender, instance, created, **kwargs):
    if created:
        instance.name = instance.file
        instance.save()
        print(instance.name)

class Associate(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_organizer = models.BooleanField(default=False, db_index=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()