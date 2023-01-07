from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


MAX_LENGTH_EMAIL = 254


class User(AbstractUser):
    """User model."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    email = models.EmailField(
        'email address',
        max_length=MAX_LENGTH_EMAIL,
        unique=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    """Subscribe model."""
    author = models.ForeignKey(
        User,
        related_name='subscribing',
        verbose_name="Author",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        related_name='subscriber',
        verbose_name="Subscriber",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-id',)
        constraints = [
            UniqueConstraint(
                fields=('user', 'author'),
                name='unique_subscription')
        ]
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'
