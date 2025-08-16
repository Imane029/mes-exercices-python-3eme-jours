# Challenge 1 : Liste de multiples
#--------------------------------------
print("\n--- Challenge 1 : Liste de multiples ---")
try:
    number = int(input("Entrez un nombre : "))
    length = int(input("Entrez une longueur : "))
    
    multiples = []
    for i in range(1, length + 1):
        multiples.append(number * i)
    
    print(multiples)

except ValueError:
    print("Veuillez entrer des nombres entiers valides.")


#--------------------------------------
# Challenge 2 : Suppression de lettres en double
#--------------------------------------
print("\n--- Challenge 2 : Suppression de lettres en double ---")
chaine_initiale = input("Entrez un mot avec des lettres consécutives en double : ")
chaine_corrigee = ""

if chaine_initiale:
    chaine_corrigee += chaine_initiale[0]
    for i in range(1, len(chaine_initiale)):
        if chaine_initiale[i] != chaine_initiale[i-1]:
            chaine_corrigee += chaine_initiale[i]

print(f"La nouvelle chaîne est : {chaine_corrigee}")
