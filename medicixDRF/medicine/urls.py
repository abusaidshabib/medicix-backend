from django.urls import path
from .views import MedicineInventoryCreateView

urlpatterns = [
    path("", MedicineInventoryCreateView.as_view()),
]
