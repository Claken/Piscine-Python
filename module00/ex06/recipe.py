cookbook = {
    'ingredients': {},
    'meal': "",
    'prep_time': 0,
}

if __name__ == "__main__":
    testbook = cookbook
    testbook['ingredients'] = {'ham', 'bread', 'cheese', 'tomatoes'}
    testbook['meal'] = 'lunch'
    testbook['prep_time'] = 10
    print(cookbook)
    print(testbook)