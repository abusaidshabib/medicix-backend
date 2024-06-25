from django.db import models
from branch.models import BaseModel

# Create your models here.
class MainCategory(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Category(BaseModel):
    maincategory = models.ForeignKey(MainCategory, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Subcategory(BaseModel):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
