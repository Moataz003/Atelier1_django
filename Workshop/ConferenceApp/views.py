from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Conference
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import ConferenceModel
def all_conferences(request):
    conferences = Conference.objects.all()
    return render(request, "liste.html", {"liste": conferences})

class ConferenceDetails(DetailView):
    model = Conference
    template_name = "conference_detail.html"
    context_object_name = "conference"

class ConferenceCreate(CreateView):
    model = Conference
    form_class = ConferenceModel
    #fields = ['name', 'description', 'theme', 'start_date', 'end_date']
    template_name = "conference_form.html"
    success_url = reverse_lazy("conference_liste")


class ConferenceUpdate(UpdateView):
    model = Conference
    #fields = ['name', 'description', 'theme', 'start_date', 'end_date']
    template_name = "conference_form.html"
    form_class = ConferenceModel
    success_url = reverse_lazy("conference_liste")

class ConferenceDelete(DeleteView):
    model = Conference
    template_name = "conference_confirm_delete.html"
    success_url = reverse_lazy("conference_liste")


