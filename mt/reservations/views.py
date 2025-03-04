from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from customers.models import Customer
from tables.models import Table
from .models import Reservation

# API: Получить список всех бронирований
def reservation_list(request):
    reservations = list(Reservation.objects.values())
    return JsonResponse(reservations, safe=False)

# API: Создать новое бронирование
@csrf_exempt
def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        customer = Customer.objects.get(id=data["customer_id"])
        table = Table.objects.get(id=data["table_id"])
        reservation = Reservation.objects.create(customer=customer, table=table, date=data["date"])
        return JsonResponse({
            "id": reservation.id, 
            "customer": reservation.customer.name, 
            "table": reservation.table.number, 
            "date": reservation.date
        })

# HTML-страница со списком бронирований
def reservation_list_view(request):
    reservations = Reservation.objects.select_related("customer", "table").all()
    return render(request, "reservations/list.html", {"reservations": reservations})
