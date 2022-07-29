import django


from django.urls import path
from . import views

urlpatterns=[
    path('read-data/',views.readData,name="read-data"),
    path('write-data/<int:pk>/',views.writeData,name="write-data"),
    path('create-data/',views.createData,name="create-data"),
    path('sensor-read/',views.sensorRead,name="sensor-read"),
    path('sensor-write/<int:pk>/',views.sensorWrite,name="sensor-write"),
]