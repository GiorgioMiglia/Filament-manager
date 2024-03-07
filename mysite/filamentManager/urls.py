from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:filament_id>/", views.detail, name="detail"),
    path('filament/<int:filament_id>/add_comment/', views.add_comment, name='add_comment'),
]