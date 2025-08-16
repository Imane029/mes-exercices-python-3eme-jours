# Exercice 1 : What is the Season?
#--------------------------------------
try:
    mois = int(input("Veuillez entrer un mois sous forme de chiffre (1 à 12) : "))
    if mois == 12 or 1 <= mois <= 2:
        print("C'est l'hiver !")
    elif 3 <= mois <= 5:
        print("C'est le printemps !")
    elif 6 <= mois <= 8:
        print("C'est l'été !")
    elif 9 <= mois <= 11:
        print("C'est l'automne !")
    else:
        print("Veuillez entrer un chiffre entre 1 et 12.")
except ValueError:
    print("Veuillez entrer un nombre valide.")

# Exercice 2 : For Loop
#--------------------------------------
print("\nAffichage de tous les nombres de 1 à 20 :")
for i in range(1, 21):
    print(i)

print("\nAffichage des éléments avec un index pair (de 0 à 19) :")
for i in range(20):
    if i % 2 == 0:
        print(i)
# Exercice 3 : While Loop
#--------------------------------------
mon_nom = "Imane"
nom_utilisateur = ""
while nom_utilisateur.lower() != mon_nom.lower():
    nom_utilisateur = input("Veuillez entrer votre nom: ")

print(f"Bonjour {mon_nom} ! Ravi de vous revoir.")
#--------------------------------------
# Exercice 4 : Check the index
#--------------------------------------
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
nom_utilisateur = input("Veuillez entrer votre nom: ")
if nom_utilisateur in names:
    index = names.index(nom_utilisateur)
    print(f"L'index de la première occurrence de votre nom est: {index}")
else:
    print("Votre nom n'est pas dans la liste.")
#--------------------------------------
# Exercice 5 : Greatest Number
#--------------------------------------
nombre1 = float(input("Entrez le 1er nombre: "))
nombre2 = float(input("Entrez le 2ème nombre: "))
nombre3 = float(input("Entrez le 3ème nombre: "))

if nombre1 >= nombre2 and nombre1 >= nombre3:
    plus_grand = nombre1
elif nombre2 >= nombre1 and nombre2 >= nombre3:
    plus_grand = nombre2
else:
    plus_grand = nombre3

print("Le plus grand nombre est:", plus_grand)
#--------------------------------------
# Exercice 6 : Random number
#--------------------------------------
import random

parties_gagnees = 0
parties_perdues = 0

while True:
    try:
        nombre_utilisateur = int(input("Devinez un nombre entre 1 et 9 (entrez '0' pour quitter) : "))
        
        if nombre_utilisateur == 0:
            break
        
        if 1 <= nombre_utilisateur <= 9:
            nombre_aleatoire = random.randint(1, 9)
            if nombre_utilisateur == nombre_aleatoire:
                print("Gagné ! C'était bien", nombre_aleatoire)
                parties_gagnees += 1
            else:
                print("Perdu. Mieux vaut se rattraper la prochaine fois.")
                parties_perdues += 1
        else:
            print("Veuillez entrer un nombre entre 1 et 9.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")

print(f"\nVous avez gagné {parties_gagnees} parties et perdu {parties_perdues} parties.")

