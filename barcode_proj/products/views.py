from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse
from .models import Product
from .forms import ProductForm


def index(request):
	form = ProductForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect(reverse('barcode-img', kwargs={
				'id': form.instance.id
				}))

	return render(request, 'index.html', {'form':form})



def barcode_img(request, id):
	objects = get_object_or_404(Product, id=id)
	return render(request, 'barcode.html', {'objects':objects})
