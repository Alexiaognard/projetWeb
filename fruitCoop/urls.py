from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('read/account', views.read_myaccount, name='myaccount'),
    path('read/exports', views.read_myexport, name='myexport'),
    path('create/export', views.create_export, name='create_export'),
    path('update/export/<int:numexport>', views.update_myexport, name='update_myexport'),
    path('read/room', views.read_myroom, name='myroom'),
    path('read/rooms',views.read_rooms, name='rooms'),
    path('read/member_room', views.read_memberbyroom, name='read_memberbyroom'),
    path('update/member', views.update_member, name='update_member'),
    path('addRoom', views.addroom, name='addRoom'),
    path('search', views.search, name="search"),
    path('search/<str:keyword>/<int:page>', views.search, name="search"),
    path('delete/export/<int:numexport>', views.delete_myexport, name="delete_export"),
    path('create/exportform', views.create_exportform, name="create_exportform"),
    path('read/exportforms', views.read_exportform, name="read_exportform"),
    path('update/exportform/<int:numform>/', views.update_myexportform, name='update_exportform'),
    path('delete/exportform/<int:numform>/', views.delete_myexportform, name="delete_exportform"),
    path('dashboard', views.dashboard, name='dashboard'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
