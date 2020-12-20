from django.contrib import admin
from .models import Recipe
from .models import Diary
from .models import Food
from .models import Slide

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Diary)
admin.site.register(Food)
admin.site.register(Slide)
