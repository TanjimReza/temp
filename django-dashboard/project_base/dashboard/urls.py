
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('room',views.room,name='room'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pk>',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>',views.deleteRoom,name='delete-room'),
    path('login/',views.login,name='login'),
    path('download/',views.download,name='download'),
    path('secretsheet/',views.secretsheet,name='secretsheet'),
    path('secretsheetresult/',views.secretsheet,name='secretsheetresult'),
]
