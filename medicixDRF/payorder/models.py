from django.db import models

from branch.models import BaseModel


ORDER_TYPE = [
        ("on","Online"),
        ("off","Offline")
    ]


class Order(BaseModel):
    medicine = models.ForeignKey("medicine.Medicine", on_delete=models.CASCADE)
    branch = models.ForeignKey("branch.Branch", on_delete=models.CASCADE)
    ordered_by = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    order_type = models.CharField(max_length=50,  choices=ORDER_TYPE)

    def __str__(self):
        return self.name

PAYMENT_METHODS = [
    ("bkash","Bkash"),
    ("dbl","Dutch Bangla Bank"),
    ("nagad","Nagad")
]

class Payments(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    delivery_status = models.BooleanField()
    due = models.FloatField()
