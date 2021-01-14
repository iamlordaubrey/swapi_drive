from django.urls import path

from starships import views

urlpatterns = [
    path('api/starship/', views.StarshipList.as_view()),
]