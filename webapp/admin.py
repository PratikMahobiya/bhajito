from django.contrib import admin
from .models import User,UserManager,customer,Restaurant
from django.conf import settings

# Register your models here.
admin.site.register(User)
admin.site.register(customer)
admin.site.register(Restaurant)
