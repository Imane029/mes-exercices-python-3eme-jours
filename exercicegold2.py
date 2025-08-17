#exercice 1

birthdays = {
    "Alice": "1990/05/15",
    "Bob": "1988/11/22",
    "Charlie": "1995/03/10",
    "Diana": "1992/07/04",
    "Evan": "1991/09/28"
}

print("Bienvenue !")
print("Vous pouvez chercher les anniversaires des personnes dans la liste.")
nom_recherche = input("Entrez le nom d'une personne : ")

if nom_recherche in birthdays:
    anniversaire = birthdays[nom_recherche]
    print(f"L'anniversaire de {nom_recherche} est le {anniversaire}.")
else:
    print(f"Désolé, nous n'avons pas l'anniversaire de {nom_recherche}.")

#exercice 2

birthdays = {
    "Alice": "1990/05/15",
    "Bob": "1988/11/22",
    "Charlie": "1995/03/10",
    "Diana": "1992/07/04",
    "Evan": "1991/09/28"
}

print("Bienvenue !")
print("Vous pouvez chercher les anniversaires des personnes suivantes :")
for nom in birthdays:
    print(f"- {nom}")

nom_recherche = input("Entrez le nom d'une personne : ")

if nom_recherche in birthdays:
    anniversaire = birthdays[nom_recherche]
    print(f"L'anniversaire de {nom_recherche} est le {anniversaire}.")
else:
    print(f"Désolé, nous n’avons pas l’anniversaire de {nom_recherche}.")

#exercice 3
    def calculate_sum(X):
    s_X = str(X)
    n1 = int(s_X)
    n2 = int(s_X * 2)
    n3 = int(s_X * 3)
    n4 = int(s_X * 4)
    return n1 + n2 + n3 + n4

try:
    x = int(input("Entrez un nombre entier (X) : "))
    result = calculate_sum(x)
    print(f"La somme est : {result}")
except ValueError:
    print("Entrée invalide.")

#exercice 4

import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws = 0
    while True:
        throws += 1
        dice1 = throw_dice()
        dice2 = throw_dice()
        if dice1 == dice2:
            return throws

def main():
    try:
        num_doubles = int(input("Combien de fois voulez-vous lancer jusqu'à obtenir des doubles ? "))
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre entier.")
        return

    results = []
    total_throws = 0
    
    for _ in range(num_doubles):
        throws_to_doubles = throw_until_doubles()
        results.append(throws_to_doubles)
        total_throws += throws_to_doubles

    average_throws = total_throws / num_doubles
    
    print(f"Total des lancers pour atteindre {num_doubles} doubles : {total_throws}")
    print(f"Moyenne des lancers pour atteindre les doubles : {average_throws:.2f}")

if __name__ == "__main__":
    main()
