from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class User(AbstractUser):
    """User model."""
    email = models.EmailField(
        'email address',
        max_length=254,
        unique=True,
    )

    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]
    USERNAME_FIELD = 'email'

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
        verbose_name='Author',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        related_name='subscriber',
        verbose_name='Subscriber',
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

    def __str__(self):
        return f'{self.user} subscribe to {self.author}'
