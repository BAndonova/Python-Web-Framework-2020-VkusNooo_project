from django.shortcuts import render, redirect

from vkusnooo_app.models import Recipe
from vkusnooo_app.forms import RecipeForm


def index(request):
    if Recipe.objects.exists():
        recipes = Recipe.objects.all()
        recipes_count = recipes.count()
        context = {
            'recipes': recipes,
            'recipes_count': recipes_count
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def recipes(request):
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


def create_recipe(request):
    if request.method == 'GET':
        context = {
            'form': RecipeForm(),
        }

        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'create.html', context)


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
    # ingr = recipe.ingredients.split(',')

    if request.method == 'GET':
        context = {
            'form': RecipeForm(instance=recipe),
            'recipe': recipe,
            # 'ingr': ingr
        }

        return render(request, 'details.html', context)


def delete_recipe(request,pk):
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
    return redirect(request, 'desserts.html', context)


def meat_meals(args):
    pass


def meatless_meals(args):
    pass


def other(args):
    pass


def pasta_dough(args):
    pass


def vegan(args):
    pass


def healthy(args):
    pass
