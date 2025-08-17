

# exercice 1
manufacturers_string = input("Veuillez entrer les noms des fabricants séparés par des virgules (par ex. : Volkswagen, Toyota, Ford Motor, Honda, Chevrolet) : ")

manufacturers_list = [name.strip() for name in manufacturers_string.split(',')]

print(f"Il y a {len(manufacturers_list)} fabricants dans la liste.")

manufacturers_list.sort(reverse=True)
print("Fabricants dans l'ordre décroissant :", manufacturers_list)

o_count = 0
for name in manufacturers_list:
    if 'o' in name.lower():
        o_count += 1
print(f"Nombre de fabricants dont le nom contient la lettre 'o' : {o_count}")

i_count_not_in = 0
for name in manufacturers_list:
    if 'i' not in name.lower():
        i_count_not_in += 1
print(f"Nombre de fabricants dont le nom ne contient pas la lettre 'i' : {i_count_not_in}")

unique_manufacturers = list(set(manufacturers_list))

comma_separated_string = ", ".join(unique_manufacturers)
print("\nEntreprises sans doublons :", comma_separated_string)
print(f"Il y a maintenant {len(unique_manufacturers)} entreprises dans la liste.")

unique_manufacturers.sort()
reversed_names = [name[::-1] for name in unique_manufacturers]
print("Entreprises avec les noms inversés :", reversed_names)

# exercice 2

def get_full_name(first_name, last_name, middle_name=None):
    if middle_name:
        return f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        return f"{first_name.title()} {last_name.title()}"


first = input("Veuillez entrer le prénom : ")
middle = input("Veuillez entrer le deuxième prénom (laisser vide si non applicable) : ")
last = input("Veuillez entrer le nom de famille : ")


if middle:
    print(get_full_name(first_name=first, middle_name=middle, last_name=last))
else:
    print(get_full_name(first_name=first, last_name=last))
# exercice 3

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def to_morse(text):
    morse_text = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_text.append(MORSE_CODE_DICT[char])
        else:
            morse_text.append(char)
    return " ".join(morse_text)

def to_english(morse_code):
    english_text = []
    words = morse_code.split(' / ')
    for word in words:
        chars = word.split(' ')
        for char in chars:
            if char in REVERSE_MORSE_CODE_DICT:
                english_text.append(REVERSE_MORSE_CODE_DICT[char])
            else:
                english_text.append(char)
        english_text.append(' ')
    return "".join(english_text).strip()

print("\nExemple 3 :")
english_phrase = input("Veuillez entrer le texte à convertir en Morse : ")
morse_phrase = to_morse(english_phrase)
print(f"'{english_phrase}' en code Morse est : '{morse_phrase}'")
print(f"'{morse_phrase}' en anglais est : '{to_english(morse_phrase)}'")
    
