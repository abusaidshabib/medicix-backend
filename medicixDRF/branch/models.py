from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AddressModel(BaseModel):
    house_number = models.CharField(max_length=150, blank=True, null=True)
    holding_number = models.CharField(max_length=150, blank=True, null=True)
    street_name = models.CharField(max_length=150, blank=True, null=True)
    village = models.CharField(max_length=150, blank=True, null=True)
    post_office = models.CharField(max_length=150, blank=True, null=True)
    district = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    post_code = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        abstract = True

class Branch(models.Model):
    name = models.CharField(_("Branch Name"), max_length=250, blank=False, null=False, unique=True)
    branch_code = models.CharField(max_length=150, unique=True, blank=False)
    created_by = models.ForeignKey("authentication.User", related_name='created_branches', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BranchAddress(AddressModel):
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE)