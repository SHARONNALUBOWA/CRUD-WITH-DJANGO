from django.shortcuts import render

from rentmanagement.forms import BuildingForm


def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'login.html')


def payment_view(request):
    return render(request, 'payment.html')


def building_view(request):
    return render(request, 'building.html' )


def tenant_view(request):
    return render(request, 'tenant.html' )

def add_building_view(request):
    message =''
    if request.method == "POST":
        building_form = BuildingForm(request.POST)

        if building_form_is_valid():
            building_form.save()
            message = "Building Added Successfully"

    else:
        building_form = BuildingForm()

    context = {
        'form':building_form,
        'msg' : message
    }
    return render(request, "add_building.html", context)