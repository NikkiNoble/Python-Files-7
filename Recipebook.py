from pprint import pprint


def make_file_dictionary(file):
    """Output of the cook book as a dictionary"""
    with open(file, encoding='utf8') as f:
        cook_book = {}
        while True:
            recipe = f.readline().strip()
            if not recipe:
                break
            f.readline().strip()
            ingredients_list = []
            while True:
                ingredient_line = f.readline().strip()
                if not ingredient_line:
                    break
                ingredient = ingredient_line.split('|')
                ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
                ingredients_list.append(ingredients)
            cook_book.update({recipe: ingredients_list})
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    """"Get ingredients for cooking in the required quantity"""
    with open('recipe', encoding='utf8') as f:
        save_ing = {}
        while True:
            recipe = f.readline().strip()
            if not recipe:
                break
            f.readline().strip()
            ingredients = {}
            while True:
                ingredient_line = f.readline().strip()
                if not ingredient_line:
                    break
                ingredient = ingredient_line.split('|')
                ing_for_persons = int(ingredient[1]) * person_count
                ingredients.update({ingredient[0]: {'measure': ingredient[2], 'quantity': ing_for_persons}})
            for dish in dishes:
                if recipe == dish:
                    for recipe_key, ing_value in ingredients.items():
                        if recipe_key in save_ing:
                            for key_name, value_num in ing_value.items():
                                if key_name == 'quantity':
                                    save_ing[recipe_key][key_name] += value_num
                        else:
                            save_ing.update({recipe_key: ing_value})
        if save_ing == {}:
            print('В названии блюд ошибка!')
        else:
            pprint(save_ing)


print(make_file_dictionary('recipe'))
print('--------')
get_shop_list_by_dishes(['Утка по-пекински', 'Запеченный картофель'], 3)
print('--------')
# пример вызова функции для блюд с одинаковыми ингредиентами:
# наименование ингредиента не повторяется, количество складывается
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)


