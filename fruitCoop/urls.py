from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('myaccount', views.read_myaccount, name='myaccount'),
    path('signup', views.signup_producteur, name='signupProducteur'),
    path('signin', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('myexport', views.read_myexport, name='myexport'),
    path('myslot', views.read_myslot, name='myslot'),
    path('myroom',views.read_myroom, name='myroom')


]