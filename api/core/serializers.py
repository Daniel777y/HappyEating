from rest_framework import serializers
from .models import Recipe
from .models import Diary
from .models import Food
from .models import Slide

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = (
            'id', 'name', 'ingredients', 'picture',
            'difficulty', 'prep_time', 'prep_guide', 'owner'
        )


class DiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = (
            'id', 'title', 'introduction', 'picture', 'article_content', 'create_time', 'owner'
        )


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = (
            'id', 'name', 'simple_intro', 'food_type', 'calorie',
            'carbohydrate', 'fat', 'protein', 'cellulose', 'picture'
        )


class SlideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slide
        fields = (
            'id', 'content', 'picture'
        )
