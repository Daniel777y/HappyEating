# Generated by Django 3.1.4 on 2020-12-14 22:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_diary_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diary',
            options={'verbose_name': '日记', 'verbose_name_plural': '日记'},
        ),
        migrations.AddField(
            model_name='diary',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
