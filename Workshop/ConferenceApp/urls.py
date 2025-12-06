from django.urls import path
from . import views

urlpatterns=[
    # Conference URLs
    path("liste/", views.all_conferences, name="conference_liste"),
    path("detail/<int:pk>/", views.ConferenceDetails.as_view(), name="conference_detail"),
    path("create/", views.ConferenceCreate.as_view(), name="conference_create"),
    path("update/<int:pk>/", views.ConferenceUpdate.as_view(), name="conference_update"),
    path("delete/<int:pk>/", views.ConferenceDelete.as_view(), name="conference_delete"),
    
    # Submission URLs
    path("conference/<int:conference_id>/submissions/", views.SubmissionListView.as_view(), name="submission_list"),
    path("submission/<int:pk>/", views.SubmissionDetailView.as_view(), name="submission_detail"),
    path("conference/<int:conference_id>/submit/", views.SubmissionCreateView.as_view(), name="submission_create"),
    path("submission/<int:pk>/update/", views.SubmissionUpdateView.as_view(), name="submission_update"),
]