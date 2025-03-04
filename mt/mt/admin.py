from django.contrib import admin
from customers.models import Customer
from tables.models import Table
from reservations.models import Reservation

admin.site.register(Customer)
admin.site.register(Table)
admin.site.register(Reservation)
