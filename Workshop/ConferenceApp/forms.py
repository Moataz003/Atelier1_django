from django import forms
from .models import Conference

class ConferenceModel(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'start_date', 'end_date', 'description']
        labels = {
            'name': 'Nom de la conférence',
            'start_date': 'Date de début',
            'end_date': 'Date de fin',
        
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom de la conférence'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez une description'}),
        }