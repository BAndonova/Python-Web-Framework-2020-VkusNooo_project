from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from recipe_core.decorators import group_required
from vkusnooo_app.models import Recipe, Like
from vkusnooo_app.forms import RecipeForm
from vkusnooo_auth.models import UserProfile


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
        users = UserProfile.objects.all()
        users_count = users.count()
        context = {
            'recipes': recipes,
            'recipes_count': recipes_count,
            'users_count': users_count,
        }

        return render(request, 'all_recipes.html', context)
    else:
        return redirect('index.html')


@login_required
# @group_required(groups=['Regular Users'])
def create_recipe(request):
    if request.method == 'GET':
        instance = Recipe(created_by=request.user)
        context = {
            # 'recipes': recipes
            'form': RecipeForm(),
            'current_page': 'create',
            'created_by': instance,
            # 'show_delete': recipe.user == request.user
        }

        return render(request, 'create.html', context)

    else:
        instance = Recipe(created_by=request.user)
        form = RecipeForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
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
    # user = Recipe.created_by.get(isinstance=recipe)
    ingr = recipe.ingredients.split(',')

    recipe.can_delete = recipe.created_by_id == request.user.id

    if request.method == 'GET':
        # user = Recipe.created_by
        context = {
            'form': RecipeForm(instance=recipe),
            'recipe': recipe,
            'ingr': ingr,
            'can_delete': recipe.can_delete,
            'can_like': recipe.created_by_id != request.user.id,
            'has_liked': recipe.like_set.filter(user_id=request.user.id).exists(),
        }

        return render(request, 'details.html', context)


@login_required
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if recipe.user.user != request.user:
        # forbid
        pass
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


@login_required
def like_recipe(request, pk):
    like = Like.objects.filter(user_id=request.user.id, recipe_id=pk).first()
    if like:
        like.delete()
    else:
        recipe = Recipe.objects.get(pk=pk)
        like = Like(value="Like", user=request.user.id)
        like.recipe = recipe
        like.save()
    return redirect('details recipe', pk)
