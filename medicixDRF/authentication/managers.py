from django.contrib.auth.base_user import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not username:
            raise ValueError("Users must have an username")

        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        if password:
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(email, password=password, username=username)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
