from Animal import Animal
import random

wolf = Animal("Wolf", "Mammal", "BARK")
dog = Animal("Dog", "Mammal", "bark")
deer = Animal("Deer", "Mammal", "bellow")
bear = Animal("Bear", "Mammal", "Roar")

animals = [wolf, dog, deer,  bear]
randomAnimal = random.choice(animals)

print(randomAnimal.name)
