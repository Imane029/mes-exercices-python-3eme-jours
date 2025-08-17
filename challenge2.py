def create_letter_index_dict(word):
    letter_indices = {}
    for index, letter in enumerate(word):
        if letter in letter_indices:
            letter_indices[letter].append(index)
        else:
            letter_indices[letter] = [index]
    return letter_indices

user_word = input("Entrez un mot : ")

result = create_letter_index_dict(user_word)
print(result)
