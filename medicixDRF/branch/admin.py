# admin.py

from django.contrib import admin
from .models import Branch, BranchAddress

class BranchAddressInline(admin.StackedInline):
    model = BranchAddress
    can_delete = False
    verbose_name_plural = 'Branch Address'

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [BranchAddressInline]

@admin.register(BranchAddress)
class BranchAddressAdmin(admin.ModelAdmin):
    pass
