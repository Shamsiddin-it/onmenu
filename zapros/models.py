from django.db import models


class Category(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name

class Dish(models.Model):
    photo = models.ImageField( upload_to="static\images", height_field=None, width_field=None, max_length=None)
    name = models.CharField( max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField( max_digits=5, decimal_places=2)




    

    