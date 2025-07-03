from django.db import models

# Create your models here.

class Product(models.Model):
   name=models.CharField(max_length=50,null=False,default='product-name')
   description=models.TextField(null=False)
   price=models.DecimalField(null=False,decimal_places=2,max_digits=8)
   image=models.ImageField(upload_to='products/',default="",null=False)

   def __str__(self):
      return f'Name : {self.name} |  Price: {self.price}'
