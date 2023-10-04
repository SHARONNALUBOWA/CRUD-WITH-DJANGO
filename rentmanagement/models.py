from django.db import models


gender_options = [
    ("F", "Female"),
    ("M", "Male"),
]


class Owner(models.Model):
    owner_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=2, choices=gender_options)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=50, null=True, blank=True, default="N/A")
    
    
class Building(models.Model):
    building_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, default="N/A" )
    caretaker_name = models.CharField(max_length=50)
    caretaker_contact = models.CharField(max_length=10)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    
    
class Rental(models.Model):
    no_of_rooms = models.IntegerField
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    price = models.IntegerField
    status_options = [
        ("O", "Occupied"),
        ("V", "Vacant"),
    ]
    status = models.CharField(max_length=2, choices=status_options)
    
    
class Tenant(models.Model):
    tenant_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=2, choices=gender_options)
    contact = models.CharField(max_length=10)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)


class Payment(models.Model):
    payment_date = models.DateField(auto_now_add=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    payment_for = models.CharField(max_length=12)
    amount_paid = models.IntegerField