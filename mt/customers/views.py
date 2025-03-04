from django.http import JsonResponse
from django.shortcuts import render, redirect
from django import forms
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Customer

# Форма для ввода данных клиента
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone']

# HTML-форма для добавления клиента
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer-list')  # Перенаправление на список клиентов
    else:
        form = CustomerForm()
    return render(request, "customers/add_customer.html", {"form": form})

# API: Получить список клиентов
def customer_list(request):
    customers = list(Customer.objects.values())
    return JsonResponse(customers, safe=False)

# API: Создать клиента
@csrf_exempt
def create_customer(request):
    if request.method == "POST":
        data = json.loads(request.body)
        customer = Customer.objects.create(name=data["name"], phone=data["phone"])
        return JsonResponse({"id": customer.id, "name": customer.name, "phone": customer.phone})

# HTML-страница со списком клиентов
def customer_list_view(request):
    customers = Customer.objects.all()
    return render(request, "customers/list.html", {"customers": customers})
