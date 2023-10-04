from django.shortcuts import render


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