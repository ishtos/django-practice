from django.contrib import admin

from .models import Currency, CurrencyHistory

class CurrencyInline(admin.TabularInline):
    model = Currency

class CurrencyHistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['symbol', 'position']}),
    ]
    inlines = [CurrencyInline]
    list_display =('symbol', 'position')

admin.site.register(CurrencyHistory, CurrencyHistoryAdmin)
admin.site.register(Currency)