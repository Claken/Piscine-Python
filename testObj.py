class Person:
  def __init__(self, name, age): # permet d'assigner des valeurs à un objet
    self.name = name
    self.age = age
    
  def __str__(self): # function par défaut print l'object en string
    return f"{self.name} : {self.age} years old"
    
  def myFunc(self):
      print("My Name Is " + self.name)

class sousPerson(Person):
    def __init__(self, name, age, tester):
        # Person.__init__(self, name, age)
        super().__init__(name, age) # avec super() pas besoin d'utiliser le param Person
        self.caca = tester
    
    def print_caca(self):
        print(self.caca)


p1 = Person("John", 36)
p2 = sousPerson("Petit", 12, "lol")

print(p1)
print(p1.name)
print(p1.age)
p1.myFunc()
p1.age = 42
print(p1)
print(p2)
p2.print_caca()