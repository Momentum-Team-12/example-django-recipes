from django.urls import path
from api import views as api_views

urlpatterns = [
    path("recipes", api_views.RecipeListView.as_view(), name="api-recipes-list")
]
