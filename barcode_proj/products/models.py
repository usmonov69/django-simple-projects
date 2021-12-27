from django.db import models
import barcode
from barcode.writer import ImageWriter
from django.core.files import File
from io import BytesIO

class Product(models.Model):
	name = models.CharField(max_length=200)
	barcode = models.ImageField(upload_to='images/', blank=True)
	country_id = models.IntegerField()
	manufacturer_id = models.IntegerField()
	product_id = models.IntegerField()

	def __str__(self):
		return str(self.name)


	def save(self, *args, **kwargs):
		EAN = barcode.get_barcode_class('ean13')
		ean = EAN(f'{self.country_id}{self.manufacturer_id}{self.product_id}', writer=ImageWriter())
		buffer = BytesIO()
		ean.write(buffer)
		self.barcode.save("barcode.png", File(buffer), save=False)
		return super().save(*args, **kwargs) 











