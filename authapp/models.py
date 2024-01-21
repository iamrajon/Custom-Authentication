from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


# class based Model for Manager of CustomUser Model
class CustomUserManager(BaseUserManager):

    #method for creating new user
    def create_user(self, email, name, password=None, **extra_fields):
        """Create and save a User with the given email, name and password."""
        if not email:
            raise ValueError("User must have an email Id to Proceed")
        
        user = self.model(
            email=self.normalize_email(email),  # Normalizing Email Address
            name=name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # method for creating superuser
    def create_superuser(self, email, name, password=None, **extra_fields):

        """Create and save a superuser with given email, name and password"""
        user = self.create_user(
            email,
            name=name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Class based Model for CustomUser
class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email Id", max_length=255, unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    bio = models.TextField()
  

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    # creating instance of Manager of CustomUser Model
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]


    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    

class CustomUserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name}'s Profile"


