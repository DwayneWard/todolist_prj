from django.urls import path

from core.views import SignUp

urlpatterns = [
    path('signup/', SignUp.as_view()),
]
