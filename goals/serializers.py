from rest_framework import serializers

from core.serializers import UserSerializer
from goals.models import GoalCategory, Goal


class GoalCategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GoalCategory
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = '__all__'


class GoalCategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = GoalCategory
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = '__all__'


class GoalCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = serializers.PrimaryKeyRelatedField(queryset=GoalCategory.objects.all())

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("Не разрешено в удаленной категории")

        return value

    class Meta:
        model = Goal
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = GoalCategorySerializer()

    class Meta:
        model = Goal
        read_only_fields = ('id', 'created', 'updated', 'user')
        fields = '__all__'

    def validate_category(self, value):
        if value.is_deleted:
            raise serializers.ValidationError("Не разрешено в удаленной категории")

        if value.user != self.context["request"].user:
            raise serializers.ValidationError("Вы не владелец данной категории")

        return value
