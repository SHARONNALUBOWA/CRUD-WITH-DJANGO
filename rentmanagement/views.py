from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from rentmanagement.forms import BuildingForm,OwnerForm,RentalForm, TenantForm,PaymentForm 


from rentmanagement.models import Building,Owner, Rental, Tenant, Payment




@login_required
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

@login_required
def add_building_view(request):
    message =''
    building_form = BuildingForm()
    if request.method == "POST":
        building_form = BuildingForm(request.POST, request.FILES)

        
        if building_form.is_valid():
            building_form.save()

            message = "Building Added Successfully"

        else:
            building_form = BuildingForm()
            
    buildings = Building.objects.all()

    context = {
        'form':building_form,
        'msg' :message,
        'buildings': buildings,
        
    }
    return render(request, 'add_building.html', context)



def edit_building_view(request, building_id):
    message = ''
    building = Building.objects.get(id=building_id)

    if request.method =="POST":
        building_form = BuildingForm(request.POST, instance=building)

        if building_form.is_valid():
            building_form.save()
            message = "Changes Made Successfully"

        else:
            message = "Wrong Inputs"
    
    else:
        building_form = BuildingForm( instance= building)

    context= {
        'form':building_form,
        'building':building,
        'message': message,
    }

    return render(request, 'edit_building.html', context)

def delete_building_view(request, building_id):
    building = Building.objects.get(id=building_id)

    building.delete()

    return redirect(add_building_view)
@login_required
def add_owner_view(request):
    message = ''
    owner_form = OwnerForm()
    
    if request.method == "POST":
        owner_form = OwnerForm(request.POST)

        if owner_form.is_valid():
            owner_form.save()
            message = "Owner Added Successfully"

        else:
            message = "Error:Wrong Inputs"
    
    owners = Owner.objects.all()
    context = {
        'form':owner_form,
        'owners':owners,
        'msg': message,

    }

    return render(request, "add_owner.html", context)

def edit_owner_view(request, owner_id):
    message = ''
    owner = Owner.objects.get(id=owner_id)

    if request.method =="POST":
        owner_form = OwnerForm(request.POST, instance=owner)

        if owner_form.is_valid():
            owner_form.save()
            message = "Changes Made Successfully"

        else:
            message = "Error:Wrong Inputs"
    
    else:
        owner_form = OwnerForm( instance= owner)
        

    context= {
        'form':owner_form,
        'owner':owner,
        'message':message,
    }

    return render(request, 'edit_owner.html', context)



def delete_owner_view(request, owner_id):
    owner = Owner.objects.get(id=owner_id)

    owner.delete()

    return redirect(add_owner_view)

@login_required
def add_rental_view(request):
    message = ''
    rental_form = RentalForm()
    
    
    if request.method == "POST":
        rental_form = RentalForm(request.POST)

        if rental_form.is_valid():
            rental_form.save()
            message = "Rental Added Successfully"

        else:
            message = "Error:Wrong Inputs"

    rentals = Rental.objects.all()
    context = {
        'form':rental_form,
        'rentals':rentals,
        'msg' : message,

    }

    return render(request, "add_rental.html", context)

def edit_rental_view(request, rental_id):
    message = ''
    rental = Rental.objects.get(id=rental_id)

    if request.method =="POST":
        rental_form = RentalForm(request.POST, instance=rental)

        if rental_form.is_valid():
            rental_form.save()
            message = "Changes Made Successfully"

        else:
            message = "Error:Wrong Inputs"
    
    else:
        rental_form = RentalForm( instance= rental)

    context= {
        'form':rental_form,
        'rental':rental,
        'message': message,
    }

    return render(request, 'edit_rental.html', context)



def delete_rental_view(request, rental_id):
    rental = Rental.objects.get(id=rental_id)

    rental.delete()

    return redirect(add_rental_view)

@login_required
def add_tenant_view(request):
    tenant_form = TenantForm()
    message = ''
    
    if request.method == "POST":
        tenant_form = TenantForm(request.POST)

        if tenant_form.is_valid():
            tenant_form.save()
            message = "Tenant Added Successfully"

        else:
            
            message = "Error:Wrong Inputs"
    
    tenants = Tenant.objects.all()
    context = {
        'form':tenant_form,
        'tenants':tenants,
        'msg' : message,

    }

    return render(request, "add_tenant.html", context)

def edit_tenant_view(request, tenant_id):
    message = ''
    tenant = Tenant.objects.get(id=tenant_id)

    if request.method =="POST":
        tenant_form = TenantForm(request.POST, instance=tenant)

        if tenant_form.is_valid():
            tenant_form.save()
            message = "Changes Made Successfully"

        else:
            message = "Error:Wrong Inputs"
    
    else:
        tenant_form = TenantForm(instance= tenant)

    context= {
        'form':tenant_form,
        'tenant':tenant,
        'message': message,
    }

    return render(request, 'edit_tenant.html', context)



def delete_tenant_view(request, tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    tenant.delete()

    return redirect(add_tenant_view)

@login_required
def add_payment_view(request):
    message =''
    payment_form = PaymentForm()
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)

        
        if payment_form.is_valid():
            payment_form.save()

            message = "Payment Made Successfully"

        else:
            payment_form = PaymentForm()
            
    payments = Payment.objects.all()

    context = {
        'form':payment_form,
        'msg' :message,
        'payments': payments,
        
    }
    return render(request, 'add_payment.html', context)



def edit_payment_view(request, payment_id):
    message = ''
    payment = Payment.objects.get(id=payment_id)

    if request.method =="POST":
        payment_form = PaymentForm(request.POST, instance=payment)

        if payment_form.is_valid():
            payment_form.save()
            message = "Changes Made Successfully"

        else:
            message = "Wrong Inputs"
    
    else:
        payment_form = PaymentForm( instance= payment)

    context= {
        'form':payment_form,
        'payment':payment,
        'message': message,
    }

    return render(request, 'edit_payment.html', context)

def delete_payment_view(request, payment_id):
    payment = Payment.objects.get(id=payment_id)

    payment.delete()

    return redirect(add_payment_view)

def sign_up_view(request):
    if request.method == "POST":
        message = ""
        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()
            message = 'User Created Successfully'

        else:
            message = 'Something Went Wrong'
    else:
        sign_up_form = UserCreationForm()

    context ={
        'form': sign_up_form,
        'message':message,
    }

    return render(request, 'registration/sign_up.html', context )





        

    

