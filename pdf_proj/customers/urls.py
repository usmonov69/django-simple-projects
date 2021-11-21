from django.urls import path
from . import views

app_name = 'customers'

urlpatterns  = [
	path('' , views.CustomerListView.as_view(), name='customer-view'),
	path('pdf/<pk>', views.customer_render_pdf_view, name='customer-pdf-view'),
	path('test/', views.render_pdf_view, name='test-view'),
]