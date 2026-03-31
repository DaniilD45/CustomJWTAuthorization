from django.db import models
from django.contrib.auth.models import AbstractUser

from orders_api.models import DeliveryType


class User(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    email = models.EmailField(unique=True)
    role = models.ForeignKey(
        'Role',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Role(models.Model):
    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class AccessRule(models.Model):
    class Meta:
        verbose_name = 'AccessRule'
        verbose_name_plural = 'AccessRules'
        unique_together = (('role', 'type'),)

    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=DeliveryType.choices, default=DeliveryType.REGULAR)


class RefreshToken(models.Model):
    class Meta:
        verbose_name = 'RefreshToken'
        verbose_name_plural = 'RefreshTokens'

    token = models.TextField(unique=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)
