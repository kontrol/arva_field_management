from django.db import models

# Create your models here.

class ChannelPartner(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    channel_partner = models.ForeignKey(ChannelPartner, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact_person = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Field(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=200)
    field_location = models.CharField(max_length=200)
    acreage = models.FloatField()
    field_type = models.CharField(max_length=200)

    def __str__(self):
        return self.field_name


