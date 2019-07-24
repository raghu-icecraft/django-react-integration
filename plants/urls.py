from django.urls import path
from . import views
urlpatterns = [
    path('api/plant/', views.PlantListCreate.as_view() ),
]