from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLE = (
    ('admin', 'admin'),
    ('moderator', 'moderator'),
    ('user', 'user'),
)


class User(AbstractUser):
    """Кастомизируем модель User."""
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

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    class Meta:
        ordering = ('-date_joined',)

    def save(self, *args, **kwargs):
        if self.role == 'admin':
            self.is_staff = True
        super().save(*args, **kwargs)
