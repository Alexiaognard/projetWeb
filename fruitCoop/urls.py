from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('myaccount', views.read_myaccount, name='myaccount'),
    path('signup', views.signup_producteur, name='signupProducteur'),
    path('signin', views.login_user, name='signinProducteur'),
    path('logout', views.logout_user, name='logout'),

]