shopping_list = {}


def add_item(key, value=1):
    if shopping_list.get(key):
        shopping_list[key] += value
    else:
        shopping_list[key] = value


add_item("Bread", 10)
add_item("Potato", 5)
add_item("Milk")
add_item("Orange", 3)
add_item("Orange", 2)
add_item("Milk")
add_item("Bread", 3)

print(shopping_list)
