from django.db import models

# Create your models here.

class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', '容易'),
        ('Medium', '中等'),
        ('Hard', '困难'),
    )
    name = models.CharField(max_length=120, verbose_name='名称')
    ingredients = models.CharField(max_length=400, verbose_name='食材')
    picture = models.FileField(verbose_name='图片')
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10,
                                  verbose_name='制作难度')
    prep_time = models.PositiveIntegerField(verbose_name='准备时间')
    prep_guide = models.TextField(verbose_name='制作指南')
  
    class Meta:
        verbose_name = '食谱'
        verbose_name_plural = '食谱'
  
    def __str__(self):
        return '{} 的食谱'.format(self.name)


class Diary(models.Model):
    title = models.CharField(max_length=120, verbose_name='标题')
    picture = models.FileField(verbose_name='图片')
    article_content = models.TextField(verbose_name='正文')
    author = models.CharField(max_length=120, verbose_name='作者')


class Food(models.Model):
    FOOD_TYPE = (
        ('Meat', '肉类'),
        ('Beans', '豆类'),
        ('Aquatic_products', '水产品'),
        ('Dairy_products', '乳制品'),
        ('Beverage', '饮品'),
        ('Fruit_vegetable', '果蔬')
    )
    name = models.CharField(max_length=120, verbose_name='名称')
    simple_intro = models.TextField(verbose_name='简单介绍')
    food_type = models.CharField(choices=FOOD_TYPE, max_length=20,
                                  verbose_name='食品类型')
    calorie = models.FloatField(verbose_name='卡路里');
    carbohydrate = models.FloatField(verbose_name='碳水化合物');
    fat = models.FloatField(verbose_name='脂肪');
    protein = models.FloatField(verbose_name='蛋白质');
    cellulose = models.FloatField(verbose_name='纤维素');
    picture = models.FileField(verbose_name='图片')

    class Meta:
        verbose_name = '食品'
        verbose_name_plural = '食品'
  
    def __str__(self):
        return '食品：{}'.format(self.name)
