from django.urls import path
from .views import UsersView, UserRegistrationView

urlpatterns = [
    path("register/", UserRegistrationView.as_view()),
    path("users/", UsersView.as_view())
]
