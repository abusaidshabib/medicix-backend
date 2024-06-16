from django.db import models
from branch.models import BaseModel

# Create your models here.
class Category(BaseModel):
    name = models.CharField( max_length=255)

    def __str__(self):
        return self.name

class Subcategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField( max_length=255)

    def __str__(self):
        return self.name
