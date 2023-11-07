from django.forms import ModelForm

from rentmanagement.models import Building, Owner, Tenant, Payment, Rental

class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = '__all__'

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'

class TenantForm(ModelForm):
    class Meta:
        model = Tenant
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'



