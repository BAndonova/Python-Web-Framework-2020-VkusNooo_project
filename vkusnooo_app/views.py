import djclick as click
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from recipe_core.decorators import group_required
from vkusnooo_app.models import Recipe, Like
from vkusnooo_app.forms import RecipeForm
from vkusnooo_auth.models import UserProfile
from vkusnooo_auth.views import user_count


def index(request):
    if Recipe.objects.exists():
        recipes = Recipe.objects.all()
        recipes_count = recipes.count()
        users_all = UserProfile.objects.all()
        users_count = users_all.count()

        # for recipe in recipes:
        #     recipe.can_delete = recipe.created_by_id == request.user.id

        context = {
            'recipes': recipes,
            'recipes_count': recipes_count,
            # 'can_delete': recipe.can_delete,
            'users_count': users_count,
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def all_recipes(request):
    if Recipe.objects.exists():
        recipes = Recipe.objects.all()
        recipes_count = recipes.count()
        users_all = UserProfile.objects.all()
        users_count = users_all.count()

        context = {
            'recipes': recipes,
            'recipes_count': recipes_count,
            'users_count': user_count,
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
            'form': RecipeForm(),
            'current_page': 'create',
            'created_by': instance,

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

    if recipe.created_by_id == request.user.id or request.user.is_superuser:
        recipe.can_delete = True
    else:
        recipe.can_delete = False

    if request.method == 'GET':
        context = {
            'form': RecipeForm(instance=recipe),
            'recipe': recipe,
            'can_delete': recipe.can_delete
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
    ingredients = recipe.ingredients.split(',')

    if recipe.created_by_id == request.user.id or request.user.is_superuser:
        recipe.can_delete = True
    else:
        recipe.can_delete = False

    if request.method == 'GET':
        # user = Recipe.created_by
        context = {
            'form': RecipeForm(instance=recipe),
            'recipe': recipe,
            'ingredients': ingredients,
            'can_delete': recipe.can_delete,
            'can_like': recipe.created_by_id != request.user.id or request.user.is_superuser,
            'has_liked': recipe.like_set.filter(user_id=request.user.id, value=True),
            'likes_count': recipe.like_set.filter(value=True).count(),
            'current_page': 'all recipes',
        }

        return render(request, 'details.html', context)


@login_required
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if recipe.created_by_id != request.user or request.user.is_superuser:
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
    recipes = Recipe.objects.filter(type='Desserts')
    context = {
        'recipes': recipes,
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
    recipes = Recipe.objects.filter(type='Pasta and Dough')

    context = {
        'recipes': recipes,
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
    likes = Like.objects.filter(recipe_id=pk).all()
    user_like = likes.filter(user_id=request.user.userprofile.id).first()
    if user_like and user_like.value == True:
        Like.objects.filter(recipe_id=pk, user_id=request.user.userprofile.id).update(value=False)

    elif user_like and user_like.value == False:
        Like.objects.filter(recipe_id=pk, user_id=request.user.userprofile.id).update(value=True)

    else:
        # recipe = Recipe.objects.get(pk=pk)
        like = Like(value=True, user_id=request.user.id, recipe_id=pk)
        # likes.recipe = recipe
        like.save()
    return redirect('details recipe', pk)

# @login_required
# def like_recipe(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     if recipe.user.user != request.user:
#         # forbid
#         pass
#     if request.method == 'GET':
#         like = Like.objects.filter(user_id=request.user.id, recipe_id=pk).first()
#         context = {
#             'form': RecipeForm(instance=recipe),
#             'recipe': recipe,
#             'like': like
#         }
#
#         return render(request, 'details.html', context)
#     if request.method == "POST":
#         like = Like.objects.filter(user_id=request.user.id, recipe_id=pk).first()
#         if like:
#             like.delete()
#         else:
#             recipe = Recipe.objects.get(pk=pk)
#             like = Like(value="Like", user=request.user.id)
#             like.recipe = recipe
#             like.save()
#         return redirect('details recipe', pk)
