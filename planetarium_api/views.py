from rest_framework import viewsets

from planetarium_api.models import (
    PlanetariumDome,
    Reservations,
    ShowTheme,
    AstronomyShow,
    ShowSession,
    Ticket
)
from planetarium_api.serializers import (
    PlanetariumDomeSerializer,
    ReservationsSerializer,
    ShowThemeSerializer,
    AstronomyShowSerializer,
    ShowSessionSerializer,
    TicketSerializer,
)


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer


class ReservationsViewSet(viewsets.ModelViewSet):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
