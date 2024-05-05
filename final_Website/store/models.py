from django.db import models
from django.contrib.auth.models import User
import datetime

#Categories of products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name;

    class Meta:
        verbose_name_plural = 'Categories'



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    
    def __str__(self):
        return self.name;




#Customers
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, limit_choices_to={'name__in': []})
    
    
    def __str__(self):
        return self.user.username







#Customer Orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    # date = models.DateField(default=datetime.datetime.today())
    status =models.BooleanField(default=False)

    def __str__(self):
        return self.product



#Tutor Information
class Tutor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    description = models.CharField(max_length=300, default='', blank=True, null=True)
    # image = models.ImageField(upload_to='uploads/tutor/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'