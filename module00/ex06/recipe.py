cookbook = {'Sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],'meal':'lunch', 'prep_time': 10}, 
            'Cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60},
            'Salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15}
}

def delete_recipe(name):
    del cookbook[name]

if __name__ == "__main__":
    print(cookbook['Cake'])