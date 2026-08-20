from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_firstName = models.CharField(max_length=200, null=True, blank=True)
    contact_lastName = models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.contact_firstName} {self.contact_lastName}"