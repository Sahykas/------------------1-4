import os

def form_dict():
    cook_book={}
    name_dishes = []
    count_ingredients = []
    other_data = []
    ingredients = []
    with open('recipes.txt', encoding="utf-8") as f:
        data_list = []
        list_buf = []
        for line in f:
            line = line.strip()
            if line != "":
                list_buf.append(line)
            else:
                data_list.append(list_buf)
                list_buf = []
    for data in data_list:
        name_dishes.append(data[0])
        count_ingredients.append(int(data[1]))
        other_data.append(data[2:])
    for data in other_data:
        for i in data:
            ingredients.append(i.split(" | "))
    for dishes in name_dishes:
        cook_book[dishes] = []
    count = 0
    for key, value in cook_book.items():
        for i in range(0, count_ingredients[count]):
            buf = {'ingredients_name': ingredients[i][0], 'quantity': int(ingredients[i][1]), 'measure': ingredients[i][2]}
            value.append(buf)
        count += 1
    return cook_book
def get_shop_list_by_dishes(dishes, person):
    dict_ingredients={}
    for dish in dishes:
        for i in range(len(cook_book[dish])):
            if cook_book[dish][i]['ingredients_name'] not in dict_ingredients.keys():
                dict_ingredients[cook_book[dish][i]['ingredients_name']]={'measure': cook_book[dish][i]['measure'], 'quantity': person*cook_book[dish][i]['quantity']}
            else:
                dict_ingredients[cook_book[dish][i]['ingredients_name']]['quantity']+=(person*cook_book[dish][i]['quantity'])
    return dict_ingredients

cook_book=form_dict()
print(cook_book)
d=get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2)
print(d)