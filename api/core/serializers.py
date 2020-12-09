from rest_framework import serializers
from .models import Recipe
from .models import Diary
from .models import Food

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = (
            'id', 'name', 'ingredients', 'picture',
            'difficulty', 'prep_time', 'prep_guide'
        )


class DiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = (
            'id', 'title', 'picture', 'article_content', 'author'
        )


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = (
            'id', 'name', 'simple_intro', 'food_type', 'calorie',
            'carbohydrate', 'fat', 'protein', 'cellulose', 'picture'
        )
