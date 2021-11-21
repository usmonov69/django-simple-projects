from django.db import models
import barcode
from barcode.writer import ImageWriter
from django.core.files import File
from io import BytesIO

class Product(models.Model):
	name = models.CharField(max_length=200)
	barcodee = models.ImageField(upload_to='images/', blank=True)
	country_id = models.CharField(max_length=1)
	manufacturer_id = models.CharField(max_length=6)
	product_id = models.CharField(max_length=5)

	def __str__(self):
		return str(self.name)


	def save(self, *args, **kwargs):
		EAN = barcode.get_barcode_class('ean13')
		ean = EAN(f'{self.country_id}{self.manufacturer_id}{self.product_id}', writer=ImageWriter())
		buffer = BytesIO()
		ean.write(buffer)
		self.barcodee.save("barcode.png", File(buffer), save=False)
		return super().save(*args, **kwargs) 











