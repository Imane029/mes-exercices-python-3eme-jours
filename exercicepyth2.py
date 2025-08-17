

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
