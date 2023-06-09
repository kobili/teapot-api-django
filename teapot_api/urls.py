"""
URL configuration for teapot_api project.

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
from users.urls import urlpatterns as user_urls
from address.urls import urlpatterns as address_urls
from payment.urls import urlpatterns as payment_urls
from banking.urls import urlpatterns as banking_urls
from category.urls import urlpatterns as category_urls
from product.urls import urlpatterns as product_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(user_urls)),
    path('', include(address_urls)),
    path('', include(payment_urls)),
    path('', include(banking_urls)),
    path('', include(category_urls)),
    path('', include(product_urls)),
]
