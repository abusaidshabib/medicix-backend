from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Branch(models.Model):
    name = models.CharField(_("Branch Name"), max_length=250, blank=False, null=False, unique=True)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    post_code = models.IntegerField()

    def __str__(self):
        return self.name
