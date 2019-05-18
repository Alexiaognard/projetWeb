from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('account', views.read_myaccount, name='myaccount'),
    path('exports', views.read_myexport, name='myexport'),
    path('create/export', views.create_export, name='create_export'),
    path('update/export/<int:numexport>', views.update_myexport, name='update_myexport'),
    path('room', views.read_myroom, name='myroom'),
    path('rooms',views.read_rooms, name='rooms'),
    path('member/room/<int:numroom>', views.read_memberbyroom, name='read_memberbyroom'),
    path('update/member', views.update_member, name='update_member'),
    path('addRoom', views.addroom, name='addRoom'),
    path('search', views.search, name="search"),
    path('search/<str:keyword>/<int:page>', views.search, name="search"),
    path('delete/export/<int:numexport>', views.delete_myexport, name="delete_export"),
    path('create/exportform', views.create_exportform, name="create_exportform"),
    path('exportforms', views.read_exportform, name="read_exportform"),
    path('update/exportform/<int:numform>/', views.update_myexportform, name='update_exportform'),
    path('delete/exportform/<int:numform>/', views.delete_myexportform, name="delete_exportform"),
    path('dashboard', views.dashboard, name='dashboard'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
