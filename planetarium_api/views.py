from rest_framework import viewsets

from planetarium_api.models import (
    PlanetariumDome,
    Reservation,
    ShowTheme,
    AstronomyShow,
    ShowSession,
    Ticket,
)
from planetarium_api.permissions import IsAdminOrIfAuthenticatedReadOnly
from planetarium_api.serializers import (
    PlanetariumDomeSerializer,
    ReservationSerializer,
    ShowThemeSerializer,
    AstronomyShowSerializer,
    ShowSessionSerializer,
    TicketSerializer,
)


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
