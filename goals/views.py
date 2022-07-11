from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from goals.models import GoalCategory
from goals.serializers import GoalCreateSerializer


class GoalCategoryCreateView(CreateAPIView):
    model = GoalCategory
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = GoalCreateSerializer
