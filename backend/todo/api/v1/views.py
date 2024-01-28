from .serializers import TaskSerializer
from rest_framework import viewsets
from ...models import Task
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    """
    for build view api in todo app
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]