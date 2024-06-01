from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import MyUserManager

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    dob = models.DateField(blank=False)

    GENDER_OPTIONS = [
        ("M", "Male"),
        ("F", "Female"),
        ("T", "Trans")
    ]

    gender = models.CharField(max_length=50, choices=GENDER_OPTIONS)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True

class MedicineProblem(models.Model):
    user = models.ManyToManyField(MyUser, verbose_name="allergic_customers")
