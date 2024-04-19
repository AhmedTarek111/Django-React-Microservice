from django.urls import path
from .views import UserLoginAPI, UserLogoutAPI ,ChangePasswordAPI ,ResetPasswordAPI ,ResendActivationCodeAPI ,SignupAPI

urlpatterns = [
    path('signup/',SignupAPI.as_view(),name='user-signup'),
    path('login/',UserLoginAPI.as_view(),name='user-login'),
    path('logout/',UserLogoutAPI.as_view(),name='user-logout'),
    path('change-password/',ChangePasswordAPI.as_view(),name='user-change-password'),
    path('activation-code/',ResendActivationCodeAPI.as_view(),name='resend-activation-code'),
    path('reset-password/',ResetPasswordAPI.as_view(),name='reset-password'),

]
