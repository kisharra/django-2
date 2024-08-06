from django.shortcuts import render



DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def multiply_recipe(recipe, servings):
    multiplied_recipe = {}
    for ingredient, amount in recipe.items():
        if isinstance(amount, (int, float)):
            multiplied_recipe[ingredient] = amount * servings
        else:
            multiplied_recipe[ingredient] = amount  # Non-numeric values, like strings, are kept unchanged
    return multiplied_recipe

def omlet(request):
    servings = int(request.GET.get('servings', 1))  # Default to 1 if not provided or invalid
    context = {
        'recipe': multiply_recipe(DATA.get('omlet', {}), servings)
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))  # Default to 1 if not provided or invalid
    context = {
        'recipe': multiply_recipe(DATA.get('pasta', {}), servings)
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get('servings', 1))  # Default to 1 if not provided or invalid
    context = {
        'recipe': multiply_recipe(DATA.get('buter', {}), servings)
    }
    return render(request, 'calculator/index.html', context)