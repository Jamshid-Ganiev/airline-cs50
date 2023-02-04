from django.urls import path

from .views import index, flight, book_flight

app_name = "flights"
urlpatterns = [
    path("", index, name="index"),
    path("<int:flight_id>", flight, name="flight"),
    path("<int:flight_id>/book", book_flight, name="book_flight")
]