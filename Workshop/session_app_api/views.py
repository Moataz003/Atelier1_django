from rest_framework import viewsets, filters
from SessionApp.models import Session
from .serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    # Partie filtrage / recherche / tri (point 7 du Workshop PDF)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ["title", "topic", "room"]
    ordering_fields = ["session_day", "start_time", "end_time"]
