from django.contrib import admin

from .models import Currency, CurrencyHistory

admin.site.register(Currency)
admin.site.register(CurrencyHistory)