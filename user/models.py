from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Email filed is required!')
        if not username:
            raise ValueError('Username field is required!')
        if not password:
            raise ValueError('Password field is required!')
        user = User.objects.create(email=self.normalize_email(email),
                                   username=username,
                                   password=password,
                                   **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)
    
    def create_superuser(self, email, username, password, **extra_fields):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(_('Email'), unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return self.email