from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Conference

def all_conferences(request):
    conferences = Conference.objects.all()
    return render(request, "liste.html", {"liste": conferences})

class ConferenceDetails(DetailView):
    model = Conference
    template_name = "conference_detail.html"
    context_object_name = "conference"

class ConferenceCreate(CreateView):
    model = Conference
    fields = ['name', 'description', 'theme', 'start_date', 'end_date']
    # Form validation
    template_name = "conference_form.html"
    # Form validation and redirection
    success_url = reverse_lazy("conference_list")


