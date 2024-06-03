from django.urls import path
from .views import UsersView, UserRegistrationView, UserLoginView

urlpatterns = [
    path("register/", UserRegistrationView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("users/", UsersView.as_view())
]
