from django.urls import path
from . import views

urlpatterns=[
    path("liste/",views.all_conferences,name="conference_liste"),
    path("detail/<int:pk>/", views.ConferenceDetails.as_view(), name="conference_detail"),
    path("create/", views.ConferenceCreate.as_view(), name="conference_create"),
    path("update/<int:pk>/", views.ConferenceUpdate.as_view(), name="conference_update"),
    path("delete/<int:pk>/", views.ConferenceDelete.as_view(), name="conference_delete"),
]