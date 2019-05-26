import datetime

from django.db import models
from django.utils import timezone


class CurrencyHistory(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    position = models.FloatField(default=.0)

    def __str__(self):
        return self.symbol


class DeleteCurrencyManager(models.Manager):
      use_for_related_fields = True
      
      def saved_within_a_week(self, **kwargs):
          now = timezone.now()
          a_week_ago = now - datetime.timedelta(days=7)
          return self.filter(saved_date__gte=a_week_ago, saved_date__lte=now)


class Currency(models.Model):
    currency_history = models.ForeignKey(CurrencyHistory, on_delete=models.PROTECT)
    symbol = models.CharField(max_length=10)
    price_change_percent = models.FloatField(default=.0)
    weighted_avg_price = models.FloatField(default=.0)
    volume = models.FloatField(default=.0)
    count = models.FloatField(default=.0)    
    saved_date = models.DateTimeField()

    def __str__(self):
        return self.symbol

    # def saved_within_a_week(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=7, seconds=1) <= self.saved_date <= now
    
    # saved_within_a_week.admin_order_field = 'saved_date'
    # saved_within_a_week.boolean = True
    # saved_within_a_week.short_description = 'Save within a week?'

    objects = DeleteCurrencyManager()

