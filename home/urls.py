from .views import HomeView, AppointmentsView, BookView, AppUpdateView, AppDeleteView
from django.urls import path

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('appointments',AppointmentsView,name = 'appointments'),
    path('book',BookView,name = 'book'),
	path('appointment/update/<int:pk>/', AppUpdateView.as_view(), name='app-update'),
	path('appointment/delete/<int:pk>/', AppDeleteView.as_view(), name='app-delete'),
]