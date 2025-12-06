from django import forms
from .models import Conference, Submission


# ============================
#    CONFERENCE FORM
# ============================

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ["name", "theme", "description", "start_date", "end_date"]
        
        labels = {
            "name": "Nom de la conférence",
            "theme": "Thème principal",
            "description": "Description",
            "start_date": "Date de début",
            "end_date": "Date de fin",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex : AI for Good"
                }
            ),

            "theme": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ajoutez une description détaillée…",
                    "rows": 4
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),

            "end_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),
        }


# ============================
#    SUBMISSION FORM
# ============================

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["title", "abstract", "keywords", "paper"]

        labels = {
            "title": "Titre",
            "abstract": "Résumé",
            "keywords": "Mots-clés",
            "paper": "Document PDF",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez le titre de votre article"
                }
            ),

            "abstract": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez le résumé",
                    "rows": 4
                }
            ),

            "keywords": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Séparez les mots-clés par des virgules"
                }
            ),

            "paper": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "accept": "application/pdf"
                }
            ),
        }
