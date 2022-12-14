from django.db import models
from accounts.manager import MyUserManager
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from rest_framework_simplejwt.tokens import RefreshToken


class SocialMedia(models.Model):
    github = models.CharField(max_length=200)
    gitlab = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    web = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'SocialMedia'
        verbose_name_plural = 'SocialMedias'
        ordering = ['id']


class User(AbstractBaseUser, PermissionsMixin):

    ROL_CHOICES = [
        ('Full-Stack', 'Full-Stack'),
        ('Front-End', 'Front-End'),
        ('Back-End', 'Back-End'),
        ('UX-UI', 'UX-UI'),
        ('Mobile', 'Mobile'),
        ('DevOps', 'DevOps'),
    ]

    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    avatar = models.ImageField(default="no-avatar.jpg", upload_to='image/users', null=True, blank=True)
    rol = models.CharField(choices=ROL_CHOICES, max_length=11)
    social = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }