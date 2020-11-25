# Generated by Django 3.1.3 on 2020-11-24 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vkusnooo_app', '0002_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='pets',
            new_name='recipe',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(blank=True, choices=[('Meat Meals', 'Meat Meals'), ('Pasta and Dough', 'Pasta and Dough'), ('Meatless Meals', 'Meatless Meals'), ('Healthy and Dietetic', 'Healthy and Dietetic'), ('Vegan', 'Vegan'), ('Desserts', 'Desserts'), ('Other', 'Other')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='video',
            field=models.ImageField(blank=True, upload_to='videos'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vkusnooo_app.recipe')),
            ],
        ),
    ]
