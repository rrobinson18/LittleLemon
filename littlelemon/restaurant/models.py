from django.db import models


# Create your models here.
# class Booking(models.Model):
#     name = models.CharField(max_length=255)
#     guest_number = models.IntegerField(null=False)
#     booking_date = models.DateField()

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)  
    inventory = models.SmallIntegerField()  

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
