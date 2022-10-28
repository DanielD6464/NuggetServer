from django.db import models

class MyModel(models.Model):
    myfield = models.CharField(max_length=200)
    
    def __str__(self):
        return self.myfield


class Vendor(models.Model):
    mac_addr = models.CharField(max_length=200, null=False)
    ip_addr = models.CharField(max_length=200, null=False)
    vendor_name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.vendor_name

