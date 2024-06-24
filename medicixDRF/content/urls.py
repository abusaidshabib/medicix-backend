from django.urls import path
from .views import CategoryGetCreateView

urlpatterns = [
    path("categories/", CategoryGetCreateView.as_view()),
]
