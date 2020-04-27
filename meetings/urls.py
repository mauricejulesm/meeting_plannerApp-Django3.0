
from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>', views.details, name="details"),
    path('rooms', views.rooms_list, name="rooms"),
]
