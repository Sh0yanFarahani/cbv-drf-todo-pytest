from rest_framework import routers
from .views import TaskViewSet
app_name = 'todo-api'

router = routers.SimpleRouter()
router.register('', TaskViewSet, basename='todo')
urlpatterns = router.urls