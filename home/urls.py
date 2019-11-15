from .views import HomeView,AppointmentsView,BookView
from django.urls import path

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('appointments',AppointmentsView,name = 'appointments'),
    path('book',BookView,name = 'book')
]