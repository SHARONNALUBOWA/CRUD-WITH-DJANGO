from django .forms import ModelForm

from rentmanagement.models import Building, Owner, Tenant, Payment, Rental

class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields='__all__'

