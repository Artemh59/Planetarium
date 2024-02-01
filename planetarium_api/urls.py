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
router.register("planetarium_dome", PlanetariumDomeViewSet)
router.register("reservation", ReservationViewSet)
router.register("show_theme", ShowThemeViewSet)
router.register("astronomy_show", AstronomyShowViewSet)
router.register("show_session", ShowSessionViewSet)
router.register("ticket", TicketViewSet)

urlpatterns = router.urls

app_name = "planetarium_api"
