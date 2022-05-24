from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Recipe
from api.serializers import RecipeSerializer


class RecipeListView(APIView):
    def get(self, request, format=None):
        """
        Return a JSON list of all recipes
        """
        recipes = Recipe.objects.filter(author=request.user)
        # add a serializer!
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
