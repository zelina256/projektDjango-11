from django.db import models

# Create your models here.
class Category(models.Model):
    category_slug = models.SlugField(unique=True, null=True, blank=True)
    category_name = models.CharField(max_length=200, null=True, blank=True)
    category_description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.category_name
class Color(models.Model):
    color_name = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.color_name
# Elementi - pakete, sherbim, produkt
class Item(models.Model):
    item_slug = models.SlugField(unique=True, null=True, blank=True)
    item_name = models.CharField(max_length=200, null=True, blank=True)
    item_description = models.TextField(null=True, blank=True)
    item_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    item_image = models.ImageField(upload_to='item_images/')
    # Many -to - one
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    # Many - to - many
    item_colors = models.ManyToManyField(Color, blank=True, null=True   )
    def __str__(self):
        return self.item_name
    

class Sale(models.Model):
    sale_p = models.IntegerField(null=True, blank=True)
    # One - to - one
    item = models.OneToOneField(Item, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.item.item_name} - {self.sale_p}%"
    
    @property
    def price_sale(self):
        if self.sale_p:
            return self.item.item_price - (self.item.item_price * self.sale_p / 100)
        return self.item.item_price
class Contact(models.Model):
    contact_firstName = models.CharField(max_length=200, null=True, blank=True)
    contact_lastName = models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.contact_firstName} {self.contact_lastName}"