from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("medicine", "branch")

@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "total_amount")