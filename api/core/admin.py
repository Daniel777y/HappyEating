from django.contrib import admin
from .models import Recipe
from .models import Diary
from .models import Food
from .models import Slide

# Register your models here.
# 食谱
admin.site.register(Recipe)
# 日记
admin.site.register(Diary)
# 食物
admin.site.register(Food)
# 轮播
admin.site.register(Slide)
