#exercice 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat_list = []
for i in range(3):
    name = input(f"Entrez le nom du chat {i+1} : ")
    age = int(input(f"Entrez l'âge de {name} : "))
    cat_list.append(Cat(name, age))

def find_oldest_cat(*cats):
    oldest_cat = None
    max_age = -1
    for cat in cats:
        if cat.age > max_age:
            max_age = cat.age
            oldest_cat = cat
    return oldest_cat

oldest = find_oldest_cat(*cat_list)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")


#exercice 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

# Création de l'objet davids_dog
davids_dog_name = input("Entrez le nom du chien de David : ")
davids_dog_height = int(input(f"Entrez la taille de {davids_dog_name} : "))
davids_dog = Dog(davids_dog_name, davids_dog_height)
print(f"David's dog's name is {davids_dog.name} and his height is {davids_dog.height}cm.")
davids_dog.bark()
davids_dog.jump()

print("-" * 20)

# Création de l'objet sarahs_dog
sarahs_dog_name = input("Entrez le nom du chien de Sarah : ")
sarahs_dog_height = int(input(f"Entrez la taille de {sarahs_dog_name} : "))
sarahs_dog = Dog(sarahs_dog_name, sarahs_dog_height)
print(f"Sarah's dog's name is {sarahs_dog.name} and his height is {sarahs_dog.height}cm.")
sarahs_dog.bark()
sarahs_dog.jump()

# Vérification du chien le plus grand
print("-" * 20)
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger.")
else:
    print("Both dogs are the same size.")


#exercice 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

print("Entrez les paroles de la chanson (tapez 'fin' pour terminer) :")
song_lyrics = []
while True:
    line = input()
    if line.lower() == 'fin':
        break
    song_lyrics.append(line)

stairway = Song(song_lyrics)
stairway.sing_me_a_song()

# exercice 4

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} est déjà dans le zoo.")

    def get_animals(self):
        if not self.animals:
            print("Aucun animal dans le zoo.")
        else:
            print(f"Animaux dans {self.name} :")
            for animal in self.animals:
                print(f"- {animal}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} a été vendu.")
        else:
            print(f"{animal_sold} n'existe pas dans le zoo.")

    def sort_animals(self):
        self.animals.sort()
        grouped_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)

        for key in grouped_animals:
            if len(grouped_animals[key]) == 1:
                grouped_animals[key] = grouped_animals[key][0]

        return grouped_animals

    def get_groups(self):
        grouped = self.sort_animals()
        if not grouped:
            print("Aucun animal à grouper.")
        else:
            print("Groupes d'animaux :")
            for key, value in grouped.items():
                print(f"{key}: {value}")


# --- Programme principal ---
zoo_name = input("Entrez le nom du zoo : ")
my_zoo = Zoo(zoo_name)

while True:
    print("\n--- Menu ---")
    print("1. Ajouter un animal")
    print("2. Afficher les animaux")
    print("3. Vendre un animal")
    print("4. Afficher les groupes")
    print("5. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        animal = input("Entrez le nom de l'animal à ajouter : ")
        my_zoo.add_animal(animal)
    elif choix == "2":
        my_zoo.get_animals()
    elif choix == "3":
        animal = input("Entrez le nom de l'animal à vendre : ")
        my_zoo.sell_animal(animal)
    elif choix == "4":
        my_zoo.get_groups()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, réessayez.")



