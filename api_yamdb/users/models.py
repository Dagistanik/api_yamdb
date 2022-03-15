from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомизируем модель User."""
    USER_ROLE = (
        ('admin', 'admin'),
        ('moderator', 'moderator'),
        ('user', 'user'),
    )
    password = models.CharField(
        'password',
        null=True,
        max_length=128,
        blank=True,
    )
    role = models.CharField(
        choices=USER_ROLE,
        max_length=20,
        default='user'
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )

    class Meta:
        ordering = ('-date_joined',)

    def save(self, *args, **kwargs):
        if self.role == 'admin':
            self.is_staff = True
        super().save(*args, **kwargs)
