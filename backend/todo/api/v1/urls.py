from rest_framework import routers
from .views import TaskViewSet
router = routers.SimpleRouter()
router.register('', TaskViewSet)
urlpatterns = router.urls