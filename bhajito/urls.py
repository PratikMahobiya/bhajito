"""bhajito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/index', views.index),
    path('customer/c_regis/', views.Customer_regis),
    path('customer/c_customer/', views.createCustomer),
    path('customer/c_profile/', views.customerProfile),
    path('restaurent/R_regis/', views.Restaurent_regis),
    path('restaurent/c_resto/', views.createResto),
    path('restaurent/r_profile/', views.restoProfile),
    path('login/', views.login),
    path('logout/', views.logout),
    path('auth/', views.auth_view),
]