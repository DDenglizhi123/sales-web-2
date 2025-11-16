from django.contrib import admin
from django.urls import path, include
from home.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('products/',include('products.urls')),
    path('contracts/',include('contracts.urls')),
    path('payments/',include('payments.urls')),
    path('deliveries/',include('deliveries.urls')),
]
