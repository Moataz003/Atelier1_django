from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.core.exceptions import PermissionDenied

from .models import Conference, Submission
from .forms import ConferenceForm, SubmissionForm
from .mixins import CommitteeRequiredMixin


# ============================
#   CONFERENCE CRUD VIEWS
# ============================

class ConferenceListView(ListView):
    model = Conference
    template_name = "liste.html"              # ← corrigé
    context_object_name = "liste"
    ordering = ["start_date"]


class ConferenceDetails(DetailView):
    model = Conference
    template_name = "conference_detail.html"  # ← corrigé
    context_object_name = "conference"


class ConferenceCreate(CommitteeRequiredMixin, CreateView):
    model = Conference
    form_class = ConferenceForm
    template_name = "conference_form.html"    # ← corrigé
    success_url = reverse_lazy("conference_liste")


class ConferenceUpdate(CommitteeRequiredMixin, UpdateView):
    model = Conference
    form_class = ConferenceForm
    template_name = "conference_form.html"    # ← corrigé
    success_url = reverse_lazy("conference_liste")


class ConferenceDelete(CommitteeRequiredMixin, DeleteView):
    model = Conference
    template_name = "conference_confirm_delete.html"  # ← corrigé
    success_url = reverse_lazy("conference_liste")



# ============================
#   SUBMISSION VIEWS
# ============================

class SubmissionListView(LoginRequiredMixin, ListView):
    model = Submission
    template_name = "submission_list.html"     # ← corrigé
    context_object_name = "submissions"

    def get_queryset(self):
        conference_id = self.kwargs.get('conference_id')
        return Submission.objects.filter(conference_id=conference_id)


class SubmissionDetailView(LoginRequiredMixin, DetailView):
    model = Submission
    template_name = "submission_detail.html"   # ← corrigé
    context_object_name = "submission"

    def get(self, request, *args, **kwargs):
        if "download" in request.GET:
            submission = self.get_object()
            response = FileResponse(submission.paper, content_type="application/pdf")
            response["Content-Disposition"] = f'attachment; filename=\"{submission.title}.pdf\"'
            return response
        return super().get(request, *args, **kwargs)


class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = "submission_form.html"     # ← corrigé

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.conference_id = self.kwargs["conference_id"]
        form.instance.status = "submitted"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("submission_list", kwargs={"conference_id": self.kwargs["conference_id"]})


class SubmissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Submission
    form_class = SubmissionForm
    template_name = "submission_form.html"     # ← corrigé

    def dispatch(self, request, *args, **kwargs):
        submission = self.get_object()

        if submission.status != "submitted":
            raise PermissionDenied("Impossible de modifier une soumission déjà acceptée ou rejetée.")

        if submission.user != request.user:
            raise PermissionDenied("Vous ne pouvez modifier que vos propres soumissions.")

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("submission_detail", kwargs={"pk": self.object.pk})
