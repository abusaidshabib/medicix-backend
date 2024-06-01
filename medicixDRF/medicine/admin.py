from django.contrib import admin

from . import models
# Register your models here.
@admin.register(models.Medicine)

class MedicineAdmin(admin.ModelAdmin):
    list_display=("id", "generic")