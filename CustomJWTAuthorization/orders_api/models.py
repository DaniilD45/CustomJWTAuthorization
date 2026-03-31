from django.db import models


class DeliveryType(models.TextChoices):
    REGULAR = 'regular', 'Обычная'
    SPECIAL = 'special', 'Специальная'


class Order(models.Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    title = models.CharField(max_length=255)
    description = models.TextField()
    delivery_type = models.CharField(max_length=255, choices=DeliveryType.choices, default=DeliveryType.REGULAR)
    creator = models.ForeignKey('auth_user_api.User', on_delete=models.CASCADE)
