# Exercice 1 : Hello World
#--------------------------------------
print("Hello world\n" * 4)

# Exercice 2 : Some Math
#--------------------------------------
resultat = (99 ** 3) * 8
print(resultat)

#--------------------------------------
# Exercice 3 : What’s your name ?
#--------------------------------------
nom_utilisateur = input("Quel est votre nom ? ")
mon_nom = "Imane"

if nom_utilisateur.lower() == mon_nom.lower():
    print("C'est incroyable ! On a le même nom. C'est peut-être le destin !")
else:
    print(f"Ah, nos noms sont différents. Heureusement, ça nous évitera de nous tromper de café le matin, {nom_utilisateur} !")

#--------------------------------------
# Exercice 4 : Tall enough to ride a roller coaster
#--------------------------------------
try:
    taille_utilisateur = int(input("Quelle est votre taille en centimètres ? "))
    hauteur_minimale = 145

    if taille_utilisateur >= hauteur_minimale:
        print("Félicitations ! Vous êtes assez grand pour faire ce tour ! Amusez-vous bien !")
    else:
        taille_manquante = hauteur_minimale - taille_utilisateur
        print(f"Désolé, il vous manque encore {taille_manquante} cm pour pouvoir monter. Continuez à bien grandir !")
except ValueError:
    print("Veuillez entrer une valeur numérique valide pour votre taille.")
#--------------------------------------
# Exercice 5 : Favorite Numbers
#--------------------------------------
my_fav_numbers = {1, 5, 8, 12, 42}
print(f"Mon ensemble initial de numéros préférés: {my_fav_numbers}")

my_fav_numbers.add(7)
my_fav_numbers.add(99)
print(f"Mon ensemble après avoir ajouté deux nouveaux numéros: {my_fav_numbers}")

last_number_removed = my_fav_numbers.pop()
print(f"Le numéro retiré est: {last_number_removed}")
print(f"Mon ensemble après avoir retiré un numéro: {my_fav_numbers}")

friend_fav_numbers = {10, 25, 42, 77}
print(f"L'ensemble des numéros préférés de mon ami: {friend_fav_numbers}")

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(f"L'ensemble de nos numéros préférés combinés: {our_fav_numbers}")
# Exercice 6 : Tuple
#--------------------------------------
tuple_ex = (1, 2, 3)
print("Il n'est pas possible d'ajouter des éléments à un tuple après sa création.")

#--------------------------------------
# Exercice 7 : List
#--------------------------------------
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(f"Panier après avoir retiré 'Banana': {basket}")
basket.remove("Blueberries")
print(f"Panier après avoir retiré 'Blueberries': {basket}")
basket.append("Kiwi")
print(f"Panier après avoir ajouté 'Kiwi': {basket}")
basket.insert(0, "Apples")
print(f"Panier après avoir ajouté 'Apples' au début: {basket}")
nb_pommes = basket.count("Apples")
print(f"Il y a {nb_pommes} pomme(s) dans le panier.")
basket.clear()
print(f"Panier après l'avoir vidé: {basket}")
#--------------------------------------
# Exercice 8 : Sandwich Orders
#--------------------------------------
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []
print("Le comptoir est en rupture de Pastrami sandwich !")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print("\nPréparation des commandes...")
while sandwich_orders:
    sandwich_en_cours = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich_en_cours)
    print(f"J'ai préparé votre {sandwich_en_cours.lower()}")
print("\nToutes les commandes ont été préparées !")
