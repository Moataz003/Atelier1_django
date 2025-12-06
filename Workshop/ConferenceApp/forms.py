from django import forms
from .models import Conference, Submission

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

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'abstract', 'keywords', 'paper']
        labels = {
            'title': 'Titre',
            'abstract': 'Résumé',
            'keywords': 'Mots-clés',
            'paper': 'Document PDF',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le titre'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez le résumé'}),
            'keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez les mots-clés, séparés par des virgules'}),
            'paper': forms.FileInput(attrs={'class': 'form-control', 'accept': 'application/pdf'}),
        }