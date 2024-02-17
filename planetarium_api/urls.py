from rest_framework.routers import DefaultRouter

from planetarium_api.views import (
    PlanetariumDomeViewSet,
    ReservationViewSet,
    ShowThemeViewSet,
    AstronomyShowViewSet,
    ShowSessionViewSet,
    TicketViewSet,
)

router = DefaultRouter()
router.register("planetariumdome", PlanetariumDomeViewSet)
router.register("reservation", ReservationViewSet)
router.register("showtheme", ShowThemeViewSet)
router.register("astronomyshow", AstronomyShowViewSet)
router.register("showsession", ShowSessionViewSet)
router.register("ticket", TicketViewSet)

urlpatterns = router.urls

app_name = "planetarium_api"
