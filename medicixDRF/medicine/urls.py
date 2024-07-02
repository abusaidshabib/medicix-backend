from django.urls import path
from .views import MedicineGetView

urlpatterns = [
    path("", MedicineGetView.as_view()),
]
