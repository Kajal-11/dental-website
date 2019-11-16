from django.shortcuts import render,redirect
from .models import Appointment
from .forms import ModelForm
from django.views.generic import DeleteView, UpdateView
# Create your views here.

def HomeView(request):
    return render(request,'index.html',{})

def BookView(request):
    form = ModelForm(request.POST or None)

    if request.method == 'POST':
        form.save()
        return redirect('appointments')

    return render(request,'contact.html',{'form':form})

def AppointmentsView(request):
    appointments = Appointment.objects.all()
    return render(request,'appointments.html',{'appointments':appointments})

class AppDeleteView(DeleteView):
    model = Appointment
    template_name = "appointment_delete.html"
    success_url = "/appointments"

class AppUpdateView(UpdateView):
    model = Appointment
    template_name = "contact.html"
    fields = ['first_name', 'last_name', 'phone', 'date', 'message']
    success_url = "/appointments"

    def form_valid(self, form):
        return super().form_valid(form)

