from django.shortcuts import render,redirect
from .models import Appointment
from .forms import ModelForm
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