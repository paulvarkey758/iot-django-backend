import django


from django.urls import path
from . import views

urlpatterns=[
    path('read-data/',views.readData,name="read-data"),
    path('write-data/<int:pk>/',views.writeData,name="write-data"),
]