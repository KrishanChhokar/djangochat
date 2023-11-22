from django.contrib import admin
from django.urls import path
from MyApp import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.loginUser,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('contact/',views.ContactPage,name='contact'),
    path('submit-successfully', views.submit_contact_form, name='submit_contact_form'),
   

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="forget_page.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="forget_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="forget_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="forget_reset_complete.html"), name='password_reset_complete'),
    
]
