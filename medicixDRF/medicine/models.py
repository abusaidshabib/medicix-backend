from django.db import models
from branch.models import BaseModel
from django.utils.translation import gettext as _

from branch.models import Branch

class Medicine(BaseModel):
    brand = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=255)
    generic = models.CharField(max_length=150)
    strength = models.CharField(max_length=150)
    subcategory = models.ForeignKey("content.Subcategory", on_delete=models.CASCADE, related_name='medicines')
    price = models.FloatField()

    TABLETS_CATEGORY = [
        ("T","Table"),
        ("SY", "Syrups"),
        ("SU", "Suspensions"),
        ("IN", "Injectables"),
        ("TO", "Topical preparations"),
        ("D", "Drops"),
        ("IN", "Inhalers"),
        ("L","Lozenges")
    ]

    MEDICINE_FOR = [
        ("H","Human"),
        ("A","Animal")
    ]
    medicine_type = models.CharField(max_length=50, choices=TABLETS_CATEGORY)
    use_for = models.CharField(max_length=50, choices=MEDICINE_FOR)
    dar = models.CharField(max_length=200)

    def __str__(self):
        return self.generic

class Inventory(BaseModel):
    medicine = models.ForeignKey(Medicine, verbose_name=_("Medicine"), on_delete=models.CASCADE, related_name='inventories')
    branch = models.ForeignKey(Branch, verbose_name=_("Branch"), on_delete=models.CASCADE)
    quantity = models.IntegerField()
    soled = models.IntegerField()
    expire_date = models.DateField()

    class Meta:
        unique_together = ["medicine", "branch"]

    def __str__(self):
        return f"{self.medicine} at {self.branch}"

    def clean(self):
        if self.soled > self.quantity:
            raise ValidationError(_("The sold quantity cannot exceed the available quantity."))