from django.urls import path
from .views import UserLoginAPI, UserLogoutAPI ,ChangePasswordAPI

urlpatterns = [
    path('login/',UserLoginAPI.as_view(),name='user-login'),
    path('logout/',UserLogoutAPI.as_view(),name='user-logout'),
    path('change-password/',ChangePasswordAPI.as_view(),name='user-change-password'),
]
