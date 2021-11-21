from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Customer

class CustomerListView(ListView):
	model  = Customer
	template_name = 'customers/main.html'

def customer_render_pdf_view(self, *args, **kwargs):
	pk = kwargs.get('pk')
	customer = Customer.objects.get( pk=pk)


	template_path = 'customers/pdf2.html'
	context = {'customer': customer,}
	# Create a Django response object, and specify content_type as pdf
	response = HttpResponse(content_type='application/pdf')
	# if download:
	# response['Content-Disposition'] = 'attachment; filename="report.pdf"'
	response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
	template = get_template(template_path)
	html = template.render(context)
    # create a pdf
	pisa_status = pisa.CreatePDF(
		html, dest=response, )
    # if error then show some funy view
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response

# Create your views here.
def render_pdf_view(request):
	template_path = 'customers/pdf1.html'
	context = {'myvar': 'this is your template context'}
	# Create a Django response object, and specify content_type as pdf
	response = HttpResponse(content_type='application/pdf')
	# if download:
	# response['Content-Disposition'] = 'attachment; filename="report.pdf"'
	response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
	template = get_template(template_path)
	html = template.render(context)
    # create a pdf
	pisa_status = pisa.CreatePDF(
		html, dest=response, )
    # if error then show some funy view
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response