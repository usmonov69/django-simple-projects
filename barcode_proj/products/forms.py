from django import forms 

from .models import Product


class ProductForm(forms.ModelForm):
	country_id  = forms.CharField(help_text="", max_length=1,
		widget=forms.TextInput(attrs={'placeholder': 'Please enter 1 numbers'}))
	manufacturer_id  = forms.CharField(min_length =6, max_length=6,
		widget=forms.TextInput(attrs={'placeholder':"Please enter 6 numbers"}))
	product_id  = forms.CharField(min_length=5, max_length=5,
		widget=forms.TextInput(attrs={'placeholder':"Please enter 5 numbers"}))

	class Meta:
		model = Product
		fields = ['name','country_id','manufacturer_id','product_id']
