# Generated by Django 3.1.3 on 2020-12-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkusnooo_auth', '0002_auto_20201206_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
