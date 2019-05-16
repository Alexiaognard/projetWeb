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
    path('create_export', views.create_export, name='create_export'),
    path('update/export/<int:numexport>', views.update_myexport, name='update_myexport'),
    path('myslot', views.read_myslot, name='myslot'),
    path('myroom', views.read_myroom, name='myroom'),
    path('rooms',views.read_rooms, name='rooms'),
    path('read_memberbyroom', views.read_memberbyroom, name='read_memberbyroom'),
    path('update_member', views.update_member, name='update_member'),
    path('addRoom', views.addroom, name='addRoom'),
    path('search/', views.search, name="search"),
    path('search/<str:keyword>/<int:page>', views.search, name="search"),


]