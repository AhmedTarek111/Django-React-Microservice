from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
    
class CustomUserManger(BaseUserManager):
    
    def create_user(self,email,password=None,**extra_fields):
        if not email :
            raise ValueError('the email Field is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
        
        
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        self.create_user(email,password=None,**extra_fields)
        
        
        

class CustomUser(AbstractUser):
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','username']
    objects = CustomUserManger()
    
    def __str__(self):
        return str(self.email)