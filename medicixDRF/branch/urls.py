from django.urls import path
from .views import BranchesCreateView, BranchGetUpdateView

urlpatterns = [
    path("", BranchesCreateView.as_view()),
    path("<str:key>/", BranchGetUpdateView.as_view())
]
