from django.contrib import admin

from planetarium_api.models import (
    PlanetariumDome,
    AstronomyShow,
    Reservation,
    ShowSession,
    ShowTheme,
    Ticket,
)

admin.site.register(PlanetariumDome)
admin.site.register(AstronomyShow)
admin.site.register(Reservation)
admin.site.register(ShowSession)
admin.site.register(ShowTheme)
admin.site.register(Ticket)
