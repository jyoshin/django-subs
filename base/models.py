from django.db import models

class Subscription(models.Model):
    sub_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField()
