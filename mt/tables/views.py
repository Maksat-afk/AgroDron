from django.http import JsonResponse
from django.shortcuts import render
from .models import Table

# API: Получить список всех столов
def table_list(request):
    tables = list(Table.objects.values())
    return JsonResponse(tables, safe=False)

# API: Получить список доступных столов
def available_tables(request):
    tables = list(Table.objects.filter(is_available=True).values())
    return JsonResponse(tables, safe=False)

# HTML-страница со списком столов
def table_list_view(request):
    tables = Table.objects.all()
    return render(request, "tables/list.html", {"tables": tables})
