# Generated by Django 3.1.4 on 2020-12-10 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_diary'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='author',
            field=models.CharField(default='Daniel', max_length=120, verbose_name='作者'),
            preserve_default=False,
        ),
    ]
