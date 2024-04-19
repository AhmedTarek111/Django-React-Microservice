from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.hashers import make_password
class CustomUserManger(BaseUserManager):
    
    def create_user(self,email,password=None,username=None,**extra_fields):
        if not email :
            raise ValueError('the email Field is required')
        
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
        
        
    def create_superuser(self,email,password=None,username=None,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if password:
            extra_fields['password']= make_password(password)
        self.create_user(email,**extra_fields)
        
        
        

class CustomUser(AbstractUser,PermissionsMixin):
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManger()
    
    def __str__(self):
        return str(self.email)