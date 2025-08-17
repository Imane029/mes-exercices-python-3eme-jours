#exercice 1

import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

    def compute_area(self):
        return math.pi * (self.radius ** 2)

    def print_definition(self):
        print("A circle is a closed two-dimensional shape in which all points on the boundary are equidistant from a central point.")

if __name__ == "__main__":
    try:
        user_radius = float(input("Veuillez entrer le rayon du cercle (laissez vide pour 1.0 par défaut) : ") or 1.0)
        my_circle = Circle(user_radius)

        print(f"\nLe rayon du cercle est : {my_circle.radius}")
        print(f"Le périmètre est : {my_circle.compute_perimeter():.2f}")
        print(f"L'aire est : {my_circle.compute_area():.2f}")
        my_circle.print_definition()
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")

#exercice 2

import random

class MyList:
    def __init__(self, letters_list):
        self.letters_list = letters_list

    def get_reversed_list(self):
        return self.letters_list[::-1]

    def get_sorted_list(self):
        return sorted(self.letters_list)

    def generate_random_list(self):
        return [random.randint(1, 100) for _ in range(len(self.letters_list))]

if __name__ == "__main__":
    user_input = input("Veuillez entrer une série de lettres séparées par des virgules (ex: a,b,c) : ")
    letters = [char.strip() for char in user_input.split(',')]
    
    my_list_obj = MyList(letters)

    print(f"\nListe originale : {my_list_obj.letters_list}")
    print(f"Liste inversée : {my_list_obj.get_reversed_list()}")
    print(f"Liste triée : {my_list_obj.get_sorted_list()}")

    random_numbers = my_list_obj.generate_random_list()
    print(f"Liste de nombres aléatoires de la même longueur : {random_numbers}")        

#exercice 3
class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice_level": "B", "gluten_index": False},
            {"name": "Hamburger", "price": 15, "spice_level": "A", "gluten_index": True},
            {"name": "Salad", "price": 18, "spice_level": "A", "gluten_index": False},
            {"name": "French Fries", "price": 5, "spice_level": "C", "gluten_index": False},
            {"name": "Beef bourguignon", "price": 25, "spice_level": "B", "gluten_index": True}
        ]

    def add_item(self, name, price, spice, gluten):
        new_dish = {
            "name": name,
            "price": price,
            "spice_level": spice,
            "gluten_index": gluten
        }
        self.menu.append(new_dish)
        print(f"'{name}' a été ajouté au menu.")

    def update_item(self, name, price, spice, gluten):
        found = False
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice_level"] = spice
                dish["gluten_index"] = gluten
                print(f"'{name}' a été mis à jour.")
                found = True
                break
        if not found:
            print(f"Erreur : Le plat '{name}' n'est pas dans le menu.")

    def remove_item(self, name):
        original_length = len(self.menu)
        self.menu = [dish for dish in self.menu if dish["name"].lower() != name.lower()]
        
        if len(self.menu) < original_length:
            print(f"'{name}' a été retiré du menu.")
            print("Menu mis à jour :")
            for dish in self.menu:
                print(dish)
        else:
            print(f"Erreur : Le plat '{name}' n'est pas dans le menu.")

def get_user_input():
    name = input("Nom du plat : ")
    try:
        price = int(input("Prix : "))
        spice = input("Niveau d'épice (A, B, C) : ").upper()
        gluten_input = input("Contient du gluten ? (oui/non) : ").lower()
        gluten = True if gluten_input == 'oui' else False
        return name, price, spice, gluten
    except ValueError:
        print("Erreur : Le prix doit être un nombre.")
        return None

if __name__ == "__main__":
    manager = MenuManager()
    
    print("Bienvenue au gestionnaire de menu.\n")
    while True:
        print("\nActions possibles :")
        print("1. Ajouter un plat")
        print("2. Mettre à jour un plat")
        print("3. Supprimer un plat")
        print("4. Afficher le menu complet")
        print("5. Quitter")

        choice = input("Veuillez choisir une action (1-5) : ")

        if choice == '1':
            print("\n--- Ajout d'un plat ---")
            item_data = get_user_input()
            if item_data:
                manager.add_item(*item_data)

        elif choice == '2':
            print("\n--- Mise à jour d'un plat ---")
            item_data = get_user_input()
            if item_data:
                manager.update_item(*item_data)
        
        elif choice == '3':
            print("\n--- Suppression d'un plat ---")
            name_to_remove = input("Nom du plat à supprimer : ")
            manager.remove_item(name_to_remove)

        elif choice == '4':
            print("\n--- Menu complet ---")
            for dish in manager.menu:
                print(dish)

        elif choice == '5':
            print("Au revoir !")
            break
        
        else:
            print("Choix invalide. Veuillez choisir un nombre entre 1 et 5.")   
