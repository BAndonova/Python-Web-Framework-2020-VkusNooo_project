# Generated by Django 3.1.3 on 2020-12-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkusnooo_app', '0002_auto_20201210_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='test',
        ),
        migrations.AddField(
            model_name='like',
            name='value',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]