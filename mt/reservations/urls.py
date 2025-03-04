from django.urls import path
from .views import reservation_list, create_reservation, reservation_list_view

urlpatterns = [
    path("api/list/", reservation_list, name="reservation-list-api"),  # API
    path("api/create/", create_reservation, name="create-reservation-api"),  # API
    path("list/", reservation_list_view, name="reservation-list"),  # HTML-страница
]
