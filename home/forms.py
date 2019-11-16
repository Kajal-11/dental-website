from django import forms
from .models import Appointment

class ModelForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 150)
    last_name = forms.CharField(max_length = 150)
    phone = forms.CharField(max_length = 150)
    date = forms.CharField(max_length = 150)
    message = forms.CharField(max_length = 150)
    class Meta:
        model = Appointment
        fields = ['first_name','last_name','phone','date','message']
    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'id': self.pk})
    
