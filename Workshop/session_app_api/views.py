from django.shortcuts import render
from rest_framework import viewsets
from SessionApp.models import Session
from Workshop.session_app_api.serialzers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    