from django.urls import path
from .views import table_list, available_tables, table_list_view

urlpatterns = [
    path("api/list/", table_list, name="table-list-api"),  # API
    path("api/available/", available_tables, name="available-tables-api"),  # API
    path("list/", table_list_view, name="table-list"),  # HTML-страница
]
