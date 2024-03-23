from django.urls import path
from .views import AddAdoption


urlpatterns = [
    path('add/', AddAdoption.as_view(), name="create_adoption")
]