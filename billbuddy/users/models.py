from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff=False, is_superuser=False, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email,  password=None, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    email = models.CharField(max_length = 255, unique = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    # created_date = models.DateField('Created date', auto_now=False, auto_now_add=True)
    # modified_date = models.DateField('Modified date', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Deleted date', null=True, blank=True)
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def natural_key(self):
        return (self.email)

    def __str__(self):
        return f'email: {self.email}'