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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



from rentmanagement.views import index_view, login_view, payment_view, building_view,tenant_view, add_building_view, add_owner_view, add_rental_view, add_tenant_view, add_payment_view, sign_up_view
from rentmanagement.views import edit_building_view
from rentmanagement.views import edit_owner_view
from rentmanagement.views import delete_building_view
from rentmanagement.views import delete_owner_view
from rentmanagement.views import edit_rental_view
from rentmanagement.views import delete_rental_view
from rentmanagement.views import edit_tenant_view
from rentmanagement.views import delete_tenant_view
from rentmanagement.views import edit_payment_view
from rentmanagement.views import delete_payment_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index_view, name='index_page'),
    path('login/', login_view, name='login_page'),
    path('payment/', payment_view, name='payment_page'),
    path('building/', building_view, name='building_page'),
    path('tenant/', tenant_view, name='tenant_page'),
    path('add_owner/', add_owner_view, name='add_owner_page'),
    path('add_building/', add_building_view, name='add_building_page'),
    path('edit_building/<int:building_id>/', edit_building_view, name='edit_building_page'),
    path('edit_owner/<int:owner_id>/', edit_owner_view, name='edit_owner_page'),
    path('delete_building/<int:building_id>/', delete_building_view, name='delete_building_page'),
    path('delete_owner/<int:owner_id>/', delete_owner_view, name='delete_owner_page'),
    path('add_rental/', add_rental_view, name='add_rental_page'),
    path('edit_rental/<int:rental_id>/', edit_rental_view, name='edit_rental_page'),
    path('delete_rental/<int:rental_id>/', delete_rental_view, name='delete_rental_page'),
    path('add_tenant/', add_tenant_view, name='add_tenant_page'),
    path('edit_tenant/<int:tenant_id>/', edit_tenant_view, name='edit_tenant_page'),
    path('delete_tenant/<int:tenant_id>/', delete_tenant_view, name='delete_tenant_page'),
    path('add_payment/', add_payment_view, name='add_payment_page'),
    path('edit_payment/<int:payment_id>/', edit_payment_view, name='edit_payment_page'),
    path('delete_payment/<int:payment_id>/', delete_payment_view, name='delete_payment_page'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
