from animals import Animal
from random import random


class Zoo:
    

    def __init__(self, capacity, budget):
        self.animals = []
        self.capacity = capacity
        self.budget = budget
        self.foods = {"meat": 4, "grass": 2}

    def accomodate_new_animal(self, animal1):
        if self.capacity == len(self.animals):
            raise ValueError("The capacity is full")
        for animal in self.animals:
            if animal.species == animal1.species and animal.name == animal1.name:
                raise ValueError("There is an animal with the same name")
        self.animals.append(animal1)

    def daily_income(self):
        return 60 * len(self.animals)
        self.budget += 30 * 60 * len(self.animals)

    def daily_outcome(self, animal, food, kilos):
        animal.eat(kilos)
        if food == "meat":
            self.budget -= kilos*self.foods["meat"]
            return kilos*self.foods["meat"]
        else:
            self.budget -= kilos*self.foods["grass"]
            return kilos*self.foods["grass"]

    def die(self, animal1):
        if animal1.die():
            self.animals.remove(animal1)
            return True
        return False

    def newborn(self, parent1, parent2, name):
        chance_gender = random()
        if chance_gender > 0.5:
            gender = "male"
        else:
            gender = "female"
        newborn = Animal(parent1.species, 0, None, gender, 4)
        self.give_name_to_newborn(name)
        self.animals.append(newborn)

    def give_name_to_newborn(self, name):
        self.name = name

    def reproduce(self, animal1, animal2, name):
        if animal1.gender != animal2.gender and animal1.species == animal2.species and not female.gestation_period:
            if animal1.age >= 2 and animal2.age >= 2:
                self.newborn(animal1, animal2)
