from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Conference

def all_conferences(request):
    conferences = Conference.objects.all()
    return render(request, "liste.html", {"liste": conferences})

class ConferenceDetails(DetailView):
    model = Conference
    template_name = "conference_detail.html"
    context_object_name = "conference"


