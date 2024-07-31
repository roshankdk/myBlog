from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Author, Post


@receiver(pre_save, sender=Post)
def create_author_if_not_exits(sender, instance, **kwargs):
    if not hasattr(instance.author, 'user'):
        user = instance.author.user
        if not Author.objects.filter(user=user).exists():
            Author.objects.create(user=user)