#--------------------------------------
# Exercice 1 : Outputs
#--------------------------------------


x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


#--------------------------------------
# Exercice 2 : Longest word without a specific character
#--------------------------------------
plus_longue_phrase = ""
print("\n--- Exercice 2 : La plus longue phrase sans la lettre 'A' ---")
while True:
    phrase_utilisateur = input("Entrez la plus longue phrase que vous pouvez, sans la lettre 'a' (ou 'q' pour quitter) : ")
    
    if phrase_utilisateur.lower() == 'q':
        print("Fin du jeu.")
        break
        
    if 'a' in phrase_utilisateur.lower():
        print("Désolé, votre phrase contient la lettre 'A'.")
    elif len(phrase_utilisateur) > len(plus_longue_phrase):
        plus_longue_phrase = phrase_utilisateur
        print(f"Félicitations ! Nouvelle plus longue phrase enregistrée : '{plus_longue_phrase}'")
    else:
        print("Votre phrase n'est pas la plus longue. Essayez encore !")


#--------------------------------------
# Exercice 3: Working on a paragraph
#--------------------------------------

import re

print("\n--- Exercice 3 : Analyse de paragraphe ---")
paragraphe = input("Veuillez saisir votre paragraphe de texte : ")

nombre_caracteres = len(paragraphe)
print(f"Le paragraphe contient {nombre_caracteres} caractères.")

nombre_phrases = len(re.split('[.!?]', paragraphe.strip())) - 1
print(f"Le paragraphe contient {nombre_phrases} phrases.")

mots = paragraphe.split()
nombre_mots = len(mots)
print(f"Le paragraphe contient {nombre_mots} mots.")

mots_uniques = set(mots)
nombre_mots_uniques = len(mots_uniques)
print(f"Le paragraphe contient {nombre_mots_uniques} mots uniques.")

nombre_non_espaces = len(paragraphe.replace(" ", "").replace("\n", ""))
print(f"Le paragraphe contient {nombre_non_espaces} caractères non-espaces.")

if nombre_phrases > 0:
    mots_par_phrase_moyenne = nombre_mots / nombre_phrases
    print(f"Il y a en moyenne {mots_par_phrase_moyenne:.2f} mots par phrase.")

nombre_mots_non_uniques = nombre_mots - nombre_mots_uniques
print(f"Le paragraphe contient {nombre_mots_non_uniques} mots non-uniques.")
