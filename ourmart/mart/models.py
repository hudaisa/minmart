from shutil import _ntuple_diskusage
from unicodedata import name
from django.db import models

# Create your models here.
class Chocolate(models.Model):
    chocolate_name = models.CharField(max_length=100)
    chocolate_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.chocolate_name

class Dairyproduct(models.Model):
    dairyproduct_name = models.CharField(max_length=100)
    dairyproduct_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)


    def __str__(self):
        return self.dairyproduct_name

class Edibleitems(models.Model):
    edibleitems_name = models.CharField(max_length=100)
    edibleitems_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.edibleitems_name        
       
class Oil_ghee(models.Model):
    oil_ghee_name = models.CharField(max_length=100)
    oil_ghee_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.oil_ghee_name

class Personal_care(models.Model):
    personal_care_name = models.CharField(max_length=100)
    personal_care_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.personal_care_name

class Spices(models.Model):
    spices_name = models.CharField(max_length=100)
    spices_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.spices_name

class Staples(models.Model):
    staples_name = models.CharField(max_length=100)
    staples_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.staples_name

class Tea_coffee(models.Model):
    tea_coffee_name = models.CharField(max_length=100)
    tea_coffee_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.tea_coffee_name

class Fruits_vegetable(models.Model):
    fruits_vegetable_name = models.CharField(max_length=100)
    fruits_vegetable_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.fruits_vegetable_name   

class Bakery_items(models.Model):
    bakery_items_name = models.CharField(max_length=100)
    bakery_items_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.bakery_items_name  

class Ready_to_eat(models.Model):
    ready_to_eat_name = models.CharField(max_length=100)
    ready_to_eat_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.ready_to_eat_name  

class Icecream_desert(models.Model):
    icecream_desert_name = models.CharField(max_length=100)
    icecream_desert_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.icecream_desert_name         

class Snacks(models.Model):
    snacks_name = models.CharField(max_length=100)
    snacks_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.snacks_name        

class Fruit_nut(models.Model):
    fruit_nut_name = models.CharField(max_length=100)
    fruit_nut_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.fruit_nut_name    

class Beverages(models.Model):
    beverages_name = models.CharField(max_length=100)
    beverages_price = models.FloatField()
    image = models.ImageField(blank=True , null = 0)

    def __str__(self):
        return self.beverages_name

class Review(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    review = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name



