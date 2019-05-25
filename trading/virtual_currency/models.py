from django.db import models
from django.utils import timezone

# class Account(models.Model):
#     free = models.FloatField(default=0)



class Currency(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    priceChangePercent = models.FloatField(default=.0)
    weightedAvgPrice = models.FloatField(default=.0)
    volume = models.FloatField(default=.0)
    count = models.FloatField(default=.0)    
    saved_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CurrencyHistory(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)