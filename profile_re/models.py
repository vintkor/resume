from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.dispatch import receiver
from django.db.models.signals import post_save
from resume.basemodel import AbstractDateModel


def set_profile_image_name(instanse, filename):
    name = get_random_string(30)
    ext = filename.split('.')[-1]
    path = 'images/profile/{}.{}'.format(name, ext)
    return path


class Profile(AbstractDateModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name='Фотография', upload_to=set_profile_image_name, blank=True, null=True, default=None)
    position = models.CharField(verbose_name='Должность', max_length=255)
    education = models.TextField(verbose_name='Образование')
    about = models.TextField(verbose_name='О себе')

    def __str__(self):
        if self.user.get_full_name() == '':
            return self.user.username
        return self.user.get_full_name()


class Hobie(AbstractDateModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class HobieUser(AbstractDateModel):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    hobie = models.ForeignKey(Hobie, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user, self.hobie)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
