# Generated by Django 3.1.3 on 2020-12-07 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vkusnooo_app', '0016_recipe_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='liked',
        ),
    ]