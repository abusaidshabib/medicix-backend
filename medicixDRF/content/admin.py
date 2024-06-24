from django.contrib import admin


from . import models
# Register your models here.

@admin.register(models.MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Subcategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category','name')
