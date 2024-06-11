from django.urls import path
from .views import UsersView, UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView, GetCSRFToken, LogoutView

urlpatterns = [
    path("csrf_cookie/", GetCSRFToken.as_view()),
    path("register/", UserRegistrationView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("profile/", UserProfileView.as_view()),
    path("users/", UsersView.as_view()),
    path("change-password/", UserChangePasswordView.as_view()),
    path("send-reset-password-email/", SendPasswordResetEmailView.as_view()),
    path("reset-password/<uid>/<token>/", UserPasswordResetView.as_view()),
]
