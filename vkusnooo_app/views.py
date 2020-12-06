from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from recipe_core.decorators import group_required
from vkusnooo_app.models import Recipe
from vkusnooo_app.forms import RecipeForm


def index(request):
    if Recipe.objects.exists():
        recipes = Recipe.objects.all()
        recipes_count = recipes.count()
        for recipe in recipes:
            recipe.can_delete = recipe.created_by_id == request.user.id

        context = {
            'recipes': recipes,
            'recipes_count': recipes_count
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def all_recipes(request):
    if Recipe.objects.exists():
        recipes = Recipe.objects.all()
        recipes_count = recipes.count()
        context = {
            'recipes': recipes,
            'recipes_count': recipes_count
        }

        return render(request, 'all_recipes.html', context)
    else:
        return redirect('index.html')


@login_required
# @group_required(groups=['Regular Users'])
def create_recipe(request):
    if request.method == 'GET':
        # recipes = Recipe.objects.all()
        # for rec in recipes:
        #     rec.image_url = rec.image.url[len('pictures'):]
        context = {
            # 'recipes': recipes
            'form': RecipeForm(),
            'current_page': 'create',
            # 'show_delete': recipe.user == request.user
        }

        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            # recipe.user = request.user
            recipe.save()
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'create.html', context)


@login_required
def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'form': RecipeForm(instance=recipe),
            'recipe': recipe,
        }

        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
            'recipe': recipe,
        }

        return render(request, 'edit.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingr = recipe.ingredients.split(',')

    recipe.can_delete = recipe.created_by_id == request.user.id

    if request.method == 'GET':
        context = {
            'form': RecipeForm(instance=recipe),
            'recipe': recipe,
            'ingr': ingr
        }

        return render(request, 'details.html', context)


@login_required
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'form': RecipeForm(instance=recipe),
            'recipe': recipe,
        }

        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')


def desserts(request):
    recipe = Recipe.objects.filter(type='Desserts')
    context = {
        'recipe': recipe,
    }
    return render(request, 'meals/desserts.html', context)


def meat_meals(request):
    recipe = Recipe.objects.filter(type='Meat Meals')
    context = {
        'recipe': recipe,
    }
    return render(request, 'meals/meat.html', context)


def meatless_meals(request):
    recipe = Recipe.objects.filter(type='Meatless Meals')
    context = {
        'recipe': recipe,
    }
    return render(request, 'meals/meatless.html', context)


def other(request):
    recipe = Recipe.objects.filter(type='Other')
    context = {
        'recipe': recipe,
    }
    return render(request, 'meals/other.html', context)


def pasta_dough(request):
    recipe = Recipe.objects.filter(type='Pasta and Dough')
    context = {
        'recipe': recipe,
    }
    return render(request, 'meals/pasta_and_dough.html', context)


def vegan(request):
    recipe = Recipe.objects.filter(type='Vegan')
    context = {
        'recipe': recipe,
    }
    return render(request, 'meals/vegan.html', context)


def healthy(request):
    recipe = Recipe.objects.filter(type='Healthy and Dietetic')
    context = {
        'recipe': recipe,
    }
    return render(request, 'meals/healthy.html', context)
