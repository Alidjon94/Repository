from django.db import models

# Create your models here.
from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table_number = models.IntegerField()
    items = models.JSONField()  # Список заказанных блюд (сами блюда и их цены)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Заказ {self.id} - Стол {self.table_number}"

    def calculate_total(self):
        self.total_price = sum(item['price'] for item in self.items)
        self.save()
