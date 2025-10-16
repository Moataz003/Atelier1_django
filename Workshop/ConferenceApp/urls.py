from django.urls import path
from . import views

urlpatterns=[
    path("liste/",views.all_conferences,name="conference_liste"),
    path("detail/<int:pk>/", views.ConferenceDetails.as_view(), name="conference_detail"),
]