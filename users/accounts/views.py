from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model 
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .serializers import CustomUserSerailzers


User = get_user_model()

class UserLoginAPI(ObtainAuthToken):
    
       def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},status=status.HTTP_200_OK)
    
class UserLogoutAPI(APIView):

    permission_classes =[IsAuthenticated]
    
    def post(self,request,*args, **kwargs):
        request.user.auth_token.delete()
        return Response({'message':'logged out'},status=status.HTTP_200_OK)
    
    
class ChangePasswordAPI(APIView):
    permission_classes =[IsAuthenticated]

    def put(self,request):
        user = request.user
        data = request.data
        if not user.check_password(data.get('old_password')):
            return Response({'old_password':'Please enter the correct old password '},status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(data.get('new_password'))
        user.save()
        
        return Response({'message':'the password changed successfully'},status=status.HTTP_200_OK)        
    
    
class ResetPasswordAPI(APIView):
    def post(self,request,*args, **kwargs):
        email = request.data.get('email')
        try:
            user= User.objects.get(email=email)
            
        except User.DoesNotExist:
            return Response({'error':'this is email not the correct email please renter the correct email'},status=status.HTTP_404_NOT_FOUND)
        mail_subject = 'Reset your password'
        current_site = get_current_site(request)
        uid = urlsafe_base64_decode(force_bytes(request.user.id))
        message = render_to_string('accounts/reset_password.html',{
            'user':request.user,
            'domain':current_site.domain,
            'uid':uid,
            'token': default_token_generator.make_token(User)
        })
        to_email = request.user.email
        send_mail(mail_subject,message,'ahmedtarekalsaudi@gmail.com',[to_email])
        return Response({'success':'the reset email has been sent'},status=status.HTTP_200_OK)
        
class ResendActivationCodeAPI(APIView):
    def post(self,request,*args, **kwargs):
        email = request.data.get('email')
        try:
            user= User.objects.get(email=email)
            
        except User.DoesNotExist:
            return Response({'error':'this is email not the correct email please renter the correct email'},status=status.HTTP_404_NOT_FOUND)
        mail_subject = 'Account Activation '
        current_site = get_current_site(request)
        uid = urlsafe_base64_decode(force_bytes(request.user.id))
        message = render_to_string('accounts/resend_activation_code.html',{
            'user':request.user,
            'domain':current_site.domain,
            'uid':uid,
            'token': default_token_generator.make_token(User)
        })
        to_email = request.user.email
        send_mail(mail_subject,message,'ahmedtarekalsaudi@gmail.com',[to_email])
        return Response({'success':'the email has been sent , please check the email please '},status=status.HTTP_200_OK)
        
        
class SignupAPI(APIView):
    def post(self,request,*args, **kwargs):
        serializer = CustomUserSerailzers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active =False
            user.save()
            
            mail_subject = 'Account Activation '
            current_site = get_current_site()
            uid = urlsafe_base64_decode(request.user.id)
            message = render_to_string('accounts/resend_activation_code.html',{
                'user':request.user,
                'domain':current_site.domain,
                'uid':uid,
                'token': default_token_generator.make_token(User)
            })
            to_email = request.user.email
            send_mail(mail_subject,message,'ahmedtarekalsaudi@gmail.com',[to_email])
            return Response({'success':'user registered successfully , please check the email please '},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    
class Profile(APIView):
    pass
