from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')