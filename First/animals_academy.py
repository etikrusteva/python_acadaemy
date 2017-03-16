class Animal(object):
    def __init__(self, color="unknown"):
        self.color = color

    def play_sound(self):
        return "\nPlay sound from animal: "

    def get_color(self):
        return self.color

class Pet(Animal):
    def __init__(self, color="unknown", name="no name"):
        self.color = color
        self.name = name
#birth_year ne e 4ast ot init za da moje da se puska stoinost, primerno 2000
        self.birth_year = 0

#definirat se getter , setter vutre v obekta za da ima polimorfizam i nasledqva6tite obekti da go polu4at
    def get_name(self):
        return self.name
#sega se obru6tame kum name koito e 4ast ot klasa, raboti se s konteksta na oebkta

    def set_name(self, name):
        self.name = name

    def get_birth_year(self):
        return self.birth_year

    def set_birth_year(self, birth_year):
        self.birth_year = int(birth_year)

#extend of class Animal(object) with class cat and class dog
class cat(Pet):
    def play_sound(self):
        return"cat sound"

class dog(Pet):
    def play_sound(self):
        return"dog sound"

list_pet = [
    dog(name='barry', color="black"),
    dog(name='rex', color="white"),
    dog(name='loly', color="grey"),
    cat(name='snowwhite', color="white"),
    cat(name='popy', color="brown"),
    dog(name='garfild', color="orange")
]

from random import randint

for item in list_pet:
    item.set_birth_year(randint(2005, 2012))
    #item
    item.get_name()
    name = item.get_name()
    item.get_color()
    color = item.get_color()
    age = 2017 - item.get_birth_year()
    print(age, name, color)






'''
animal = Animal("blue")
animal.play_sound()
my_dog = dog("white")
my_dog.play_sound()


my_cat = cat("yellow")
my_cat.play_sound()
my_dog = dog(name="Boby")



animal = Animal()
sound = animal.play_sound()
print(sound)
color = animal.get_color()
print(color)

animal_next = Animal("Red")
print("color: %s"%
        animal_next.get_color())

'''

