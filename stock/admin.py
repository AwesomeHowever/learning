from django.contrib import admin

from stock.models import Stock

from django.db import models

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "name", "description")

class Currency(models.Model):
    name = models.CharField(max_length=40)
    ticker = models.CharField(max_length=4)
    sign = models.CharField(max_length=1)

    def __str__(self):
        return self.sign

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


