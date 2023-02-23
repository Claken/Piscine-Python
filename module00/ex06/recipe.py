cookbook = {'Sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],'meal':'lunch', 'prep_time': 10}, 
            'Cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60},
            'Salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15}
}

def print_recipe_names():
    receplist = list(cookbook)
    for names in receplist:
        print(names)

def print_recipe_details(name):
    print(cookbook[name])

def delete_recipe(name):
    del cookbook[name]

def add_a_recipe():
    name = input("Enter a name: \n")
    ingredients = []
    ingredient = "test"
    print("Enter ingredients (type ENTER without writing when you done): \n")
    while ingredient != "":
        test = input()
        if test == "":
            continue
        ingredients.append(test)
    meal = input("Enter a meal type: \n")
    time = int(input("Enter a preparation time: \n"))
    cookbook[name] = {'ingredients' : ingredients, 'meal' : meal, 'prep_time' : time}

if __name__ == "__main__":
    """ print_recipe_details('Sandwich')
    print_recipe_details('Cake')
    print_recipe_details('Salad')
    delete_recipe('Cake')
    print_recipe_names() """
    add_a_recipe()
    print(cookbook)
