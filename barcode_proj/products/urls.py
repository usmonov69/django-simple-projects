from django.urls import path

from . import views

urlpatterns  = [
	path('', views.index, name='index'),
	path('barcode/<id>/', views.barcode_img, name='barcode-img')
]