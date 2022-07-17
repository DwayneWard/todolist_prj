from django.contrib import admin

from goals.models import Goal, GoalCategory

admin.site.register(Goal)
admin.site.register(GoalCategory)
