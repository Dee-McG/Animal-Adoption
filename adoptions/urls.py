from django.urls import path
from .views import AddAdoption, EditAdoption, DeleteAdoption


urlpatterns = [
    path('add/', AddAdoption.as_view(), name="create_adoption"),
    path('edit/<slug:pk>/', EditAdoption.as_view(), name="edit_adoption"),
    path('delete/<slug:pk>/', DeleteAdoption.as_view(), name="delete_adoption")
]