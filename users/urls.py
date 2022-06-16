from rest_framework import routers

from users.api_interface import ShowroomUserViewSet

router = routers.SimpleRouter()
router.register(r"showroom_user", ShowroomUserViewSet, basename="showroom_user")

urlpatterns = router.urls
