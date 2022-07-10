from django.urls import path


from core import views

urlpatterns = [
    path('signup', views.SignUp.as_view()),
    path('login', views.Login.as_view()),
    path('profile', views.ProfileView.as_view()),
]
