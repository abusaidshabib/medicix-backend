from django.contrib import admin

from . import models
# Register your models here.
@admin.register(models.Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id','doctor')

@admin.register(models.PrescriptionDetails)
class PrescriptionDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','dosage')