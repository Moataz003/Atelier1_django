from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, FileResponse
from .models import Conference, Submission
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ConferenceModel, SubmissionForm
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

# Submission Views
class SubmissionListView(LoginRequiredMixin, ListView):
    model = Submission
    template_name = "submission_list.html"
    context_object_name = "submissions"

    def get_queryset(self):
        # Filter submissions based on the conference
        conference_id = self.kwargs.get('conference_id')
        return Submission.objects.filter(conference_id=conference_id)

class SubmissionDetailView(LoginRequiredMixin, DetailView):
    model = Submission
    template_name = "submission_detail.html"
    context_object_name = "submission"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        submission = self.get_object()
        context['can_edit'] = submission.status == "submitted" and submission.user == self.request.user
        return context

    def get(self, request, *args, **kwargs):
        # Override get method to handle PDF download if requested
        if 'download' in request.GET:
            submission = self.get_object()
            response = FileResponse(submission.paper, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{submission.title}.pdf"'
            return response
        return super().get(request, *args, **kwargs)

class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = "submission_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.conference_id = self.kwargs['conference_id']
        form.instance.status = "submitted"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('submission_list', kwargs={'conference_id': self.kwargs['conference_id']})

class SubmissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Submission
    form_class = SubmissionForm
    template_name = "submission_form.html"

    def get_queryset(self):
        # Only allow updating submissions that are in "submitted" status and belong to the current user
        return Submission.objects.filter(user=self.request.user, status="submitted")

    def get_success_url(self):
        return reverse_lazy('submission_detail', kwargs={'pk': self.object.pk})
