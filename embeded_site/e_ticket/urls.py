from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('enter/<str:barcode>', views.get_barcode, name='barcode'),
]

