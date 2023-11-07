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
    def __str__(self):
        return f"{self.owner_name}-{self.gender}-{self.contact}-{self.address}"
    
    
class Building(models.Model):
    building_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, default="N/A" )
    caretaker_name = models.CharField(max_length=50)
    caretaker_contact = models.CharField(max_length=10)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.building_name}-{self.location}-{self.caretaker_name}-{self.caretaker_contact}-{self.owner}"
    
    
class Rental(models.Model):
    no_of_rooms = models.IntegerField
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    price = models.IntegerField
    status_options = [
        ("O", "Occupied"),
        ("V", "Vacant"),
    ]
    status = models.CharField(max_length=2, choices=status_options)

    def __str__(self):
        return f"{self.no_of_rooms}-{self.building}-{self.price}-{self.status}"
    
    
class Tenant(models.Model):
    tenant_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=2, choices=gender_options)
    contact = models.CharField(max_length=10)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tenant_name}-{self.gender}-{self.contact}-{self.rental}"


class Payment(models.Model):
    payment_date = models.DateField(auto_now_add=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    payment_for = models.CharField(max_length=12)
    amount_paid = models.IntegerField
    def __str__(self):
        return f"{self.payment_date}-{self.tenant}-{self.payment_for}-{self.amount_paid}"