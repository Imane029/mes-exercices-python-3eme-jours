class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-O!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = self.get_animal_types()
        animals_str = ""
        for i, animal in enumerate(animal_list):
            count = self.animals[animal]
            animal_name = animal + "s" if count > 1 else animal
            if i == len(animal_list) - 1 and i != 0:
                animals_str += " and " + animal_name
            elif i == 0:
                animals_str += animal_name
            else:
                animals_str += ", " + animal_name
        return f"{self.name}'s farm has {animals_str}."


# -------------------
# Programme principal interactif
# -------------------

farm_name = input("Entrez le nom de la ferme : ")
farm = Farm(farm_name)

while True:
    animal = input("Entrez un animal (ou 'stop' pour finir) : ").lower()
    if animal == "stop":
        break
    count = int(input(f"Combien de {animal}(s) voulez-vous ajouter ? "))
    farm.add_animal(animal, count)

print("\n--- Informations complètes ---")
print(farm.get_info())

print("\n--- Informations courtes ---")
print(farm.get_short_info())
