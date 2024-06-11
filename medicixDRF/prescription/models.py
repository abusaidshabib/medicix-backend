from django.db import models

from branch.models import BaseModel

class Prescription(BaseModel):
    user = models.ForeignKey("branch.Branch", on_delete=models.CASCADE)
    prescription_img = models.ImageField(upload_to="uploads/prescription/", height_field=None, width_field=None, max_length=None)
    doctor = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.user



class PrescriptionDetails(BaseModel):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine = models.ForeignKey("medicine.Medicine", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    dosage = models.CharField(max_length=250)
    times = models.IntegerField()

