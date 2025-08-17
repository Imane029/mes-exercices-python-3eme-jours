# exercice 1
cles = ['Dix', 'Vingt', 'Trente']
valeurs = [10, 20, 30]

nouveau_dict = dict(zip(cles, valeurs))
print(nouveau_dict)

# exercice 2
cout_total = 0
famille = {}

nb_membres = int(input("Combien de membres dans la famille ? "))
for i in range(nb_membres):
    nom = input(f"Entrez le nom du membre {i+1} : ").lower()
    age = int(input(f"Entrez l'âge de {nom} : "))
    famille[nom] = age

print("\nPrix des billets :")
for nom, age in famille.items():
    if age < 3:
        cout = 0
    elif 3 <= age <= 12:
        cout = 10
    else:
        cout = 15
    print(f"{nom.capitalize()} doit payer {cout}$.")
    cout_total += cout

print(f"\nLe coût total pour la famille est de {cout_total}$.")


# exercice 3

def describe_city(city, country="Morocco"):  
    print(f"{city} is in {country}.")

describe_city("Casablanca")
describe_city("Paris", "France")
describe_city("Reykjavik", "Iceland")

# exercice 4

import random

def deviner_nombre():
    utilisateur = int(input("Entrez un nombre entre 1 et 100 : "))
    aleatoire = random.randint(1, 100)
    if utilisateur == aleatoire:
        print("🎉 Félicitations ! Vous avez deviné le bon nombre !")
    else:
        print("❌ Dommage, ce n'est pas le bon nombre. Essayez encore !")

deviner_nombre()

# exercice 5

def make_shirt():
    taille_choisie = input("Entrez votre taille de t-shirt (S, M, L, XL) : ").upper()

    if taille_choisie == "S":
        description_taille = "small"
    elif taille_choisie == "M":
        description_taille = "medium"
    elif taille_choisie == "L":
        description_taille = "large"
    elif taille_choisie == "XL":
        description_taille = "extra large"
    else:
        description_taille = "taille inconnue"
        
    print(f"Bonjour, vous avez choisi la taille {taille_choisie}. C'est une taille {description_taille}.")

make_shirt()

# exercice 6

import random

def get_random_temp(saison):
    if saison == 'hiver':
        limite_inf = -10
        limite_sup = 16
    elif saison == 'printemps':
        limite_inf = 10
        limite_sup = 23
    elif saison == 'automne':
        limite_inf = 5
        limite_sup = 18
    elif saison == 'été':
        limite_inf = 24
        limite_sup = 40
    else:
        print("Saison invalide. Plage par défaut utilisée.")
        limite_inf = -10
        limite_sup = 40

    return random.uniform(limite_inf, limite_sup)

def main():
    saison_input = input("Veuillez entrer une saison (été, automne, hiver, ou printemps) : ").lower()
    temperature = get_random_temp(saison_input)
    print(f"\nLa température actuelle est de {temperature:.1f} degrés Celsius.")

    if temperature < 0:
        print("Brrr, il gèle ! Portez des couches supplémentaires aujourd'hui.")
    elif 0 <= temperature < 16:
        print("Un peu frais ! N'oubliez pas votre manteau.")
    elif 16 <= temperature < 24:
        print("La température est agréable, une veste légère pourrait suffire.")
    elif 24 <= temperature < 32:
        print("Il commence à faire chaud, hydratez-vous et profitez du temps !")
    else:
        print("C'est une journée chaude ! Cherchez de l'ombre et restez au frais.")

if __name__ == "__main__":
    main()

# exercice 7

data = [
    {
        "question": "Quel est le vrai nom de Baby Yoda ?",
        "answer": "Grogu"
    },
    {
        "question": "Où Obi-Wan a-t-il emmené Luke après sa naissance ?",
        "answer": "Tatooine"
    },
    {
        "question": "En quelle année est sorti le premier film Star Wars ?",
        "answer": "1977"
    },
    {
        "question": "Qui a construit C-3PO ?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker est devenu qui ?",
        "answer": "Darth Vader"
    },
    {
        "question": "De quelle espèce est Chewbacca ?",
        "answer": "Wookiee"
    }
]

def lancer_le_quiz(questions):
    reponses_correctes = 0
    reponses_incorrectes = 0
    details_mauvaises_reponses = []

    for item in questions:
        print("\n" + item["question"])
        reponse_utilisateur = input("Votre réponse : ")
        
        if reponse_utilisateur.strip().lower() == item["answer"].lower():
            reponses_correctes += 1
            print("Correct !")
        else:
            reponses_incorrectes += 1
            print(f"Incorrect. La bonne réponse est : {item['answer']}")
            details_mauvaises_reponses.append({
                "question": item["question"],
                "votre_reponse": reponse_utilisateur,
                "bonne_reponse": item["answer"]
            })
            
    return reponses_correctes, reponses_incorrectes, details_mauvaises_reponses

def afficher_resultats(correct, incorrect, mauvaises_reponses):
    print("\n--- Résultats du Quiz ---")
    print(f"Vous avez {correct} réponses correctes.")
    print(f"Vous avez {incorrect} réponses incorrectes.")

    if mauvaises_reponses:
        print("\n--- Questions auxquelles vous avez mal répondu ---")
        for detail in mauvaises_reponses:
            print(f"Question : {detail['question']}")
            print(f"Votre réponse : {detail['votre_reponse']}")
            print(f"Bonne réponse : {detail['bonne_reponse']}")
            print("-" * 20)

    if incorrect > 3:
        print("\nVous avez eu plus de 3 mauvaises réponses. Réessayez pour vous améliorer !")

if __name__ == "__main__":
    correct, incorrect, details_mauvaises = lancer_le_quiz(data)
    afficher_resultats(correct, incorrect, details_mauvaises)
