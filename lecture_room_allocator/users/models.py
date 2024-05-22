from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin




class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, course, password=None):
        if not email:
            raise ValueError('Email required')

        email = self.normalize_email(email)
        
        user = self.model(
            email=email,
            password=password,
            username=username,
            first_name=first_name,
            last_name = last_name,
            course = course,
            )
        
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password=None):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            password=password,
            )
        
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,max_length=255,blank=False)
    username = models.CharField(unique=True,max_length=255,blank=False)
    first_name = models.CharField('first name',max_length=150,blank=True)
    last_name = models.CharField('last name',max_length=150,blank=True)
    course = models.CharField('course',max_length=150,blank=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    is_superuser = models.BooleanField('superuser', default=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
  
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return self.first_name+" "+self.last_name
