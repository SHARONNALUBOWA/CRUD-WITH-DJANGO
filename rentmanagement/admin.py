from django.contrib import admin

from .models import Owner, Building, Tenant, Payment, Rental


class OwnerAdmin(admin.ModelAdmin):
    list_display = ("owner_name", "gender", "contact", "address")
    
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("building_name", "location", "caretaker_name", "caretaker_contact", "owner")
    
class RentalAdmin(admin.ModelAdmin):
    list_display = ("No of Rooms", "Building", "Price", "Status")
    
class TenantAdmin(admin.ModelAdmin):
    list_display = ("Tenant Name", "Gender", "Contact", "Rental")
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("Payment Date", "Tenant", "Payment For", "Amount Paid")
    
    
admin.site.register(Owner)
admin.site.register(Building)
admin.site.register(Tenant)
admin.site.register(Payment)
admin.site.register(Rental)