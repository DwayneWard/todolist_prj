from django.contrib import admin

from goals.models import Goal, GoalCategory, Board, BoardParticipant

admin.site.register(Goal)
admin.site.register(GoalCategory)
admin.site.register(Board)
admin.site.register(BoardParticipant)

