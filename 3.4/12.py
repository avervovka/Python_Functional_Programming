def show_list(include_quantities=True):
    for key, value in shopping_list.items():
        print(f'{value}x{key}' if include_quantities else key)


shopping_list = {'Bread': 13, 'Potato': 5, 'Milk': 2, 'Orange': 5}
show_list()
