from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext as _

from .managers import MyUserManager
from branch.models import Branch

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MyUser(BaseModel, AbstractBaseUser):
    branch = models.ForeignKey("branch.Branch", verbose_name=_("user branch"), on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(
        max_length=200,
        unique=True,
        blank=False,
        null=False
        )
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    dob = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    GENDER_OPTIONS = [
        ("M", "Male"),
        ("F", "Female"),
        ("T", "Trans")
    ]

    gender = models.CharField(max_length=50, choices=GENDER_OPTIONS)
    USERNAME_FIELD = "email"

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class MedicineProblem(BaseModel):
    user = models.ForeignKey(MyUser, verbose_name="allergic_customers", on_delete=models.CASCADE)
    medicine = models.ForeignKey("medicine.Medicine", verbose_name="name_of_medicine", on_delete=models.CASCADE)
