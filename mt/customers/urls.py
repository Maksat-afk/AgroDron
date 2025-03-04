from django.urls import path
from .views import customer_list, create_customer, customer_list_view, add_customer

urlpatterns = [
    path("api/list/", customer_list, name="customer-list-api"),  # API
    path("api/create/", create_customer, name="create-customer"),  # API
    path("list/", customer_list_view, name="customer-list"),  # HTML-страница
    path("add/", add_customer, name="add-customer"),  # Форма для добавления
]
