from rest_framework import serializers
from .models import CustomUser


class CustomUserSerailzers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','username','date_joined']