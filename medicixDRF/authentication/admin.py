from django.contrib import admin
from . import models
# Register your models here.

class UserDetailsInline(admin.StackedInline):
    model = models.UserDetails
    can_delete = False
    verbose_name_plural = 'User Details'

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    inlines = [UserDetailsInline]

@admin.register(models.UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(models.MedicineProblem)
class MedicineProblemAdmin(admin.ModelAdmin):
    pass