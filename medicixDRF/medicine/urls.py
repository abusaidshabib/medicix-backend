from django.urls import path
from .views import MedicineGetCreateView, MedicineInventoryCreateView

urlpatterns = [
    path("", MedicineGetCreateView.as_view()),
    path("inventory/", MedicineInventoryCreateView.as_view()),
]
