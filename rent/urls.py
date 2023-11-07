"""
URL configuration for rent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rentmanagement.views import index_view
from rentmanagement.views import login_view
from rentmanagement.views import payment_view
from rentmanagement.views import building_view
from rentmanagement.views import tenant_view
from rentmanagement.views import add_building_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index_page'),
    path('login/', login_view, name='login_page'),
    path('payment/', payment_view, name='payment_page'),
    path('building/', building_view, name='building_page'),
    path('tenant/', tenant_view, name='tenant_page'),
    path('add_building/', tenant_view, name='add_building_page')
]
