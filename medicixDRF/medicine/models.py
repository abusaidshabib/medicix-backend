from django.db import models
from authentication.models import BaseModel
from django.utils.translation import gettext as _

class Medicine(BaseModel):
    branch = models.ForeignKey("branch.Branch", verbose_name=_("user branch"), on_delete=models.CASCADE, null=True)
    brand = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=255)
    generic = models.CharField(max_length=150)
    strength = models.CharField(max_length=150)

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

    category = models.CharField(max_length=200, choices=TABLETS_CATEGORY)
    price = models.FloatField()

    MEDICINE_FOR = [
        ("H","Human"),
        ("A","Animal")
    ]

    use_for = models.CharField(max_length=50)
    dar = models.CharField(max_length=200)
    total = models.FloatField()
    expire_date = models.DateField()

    def __str__(self):
        return self.generic