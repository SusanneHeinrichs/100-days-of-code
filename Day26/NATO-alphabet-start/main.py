#TODO 1. Create a dictionary in this format:

phonetic_dict = {row[0] : row[1] for _, row in pandas.read_csv('NATO-alphabet-start/nato_phonetic_alphabet.csv').iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("What is your name?:")
print("Your name spelled with the phonetic alphabet is:")
for letter in name.upper():
    print(phonetic_dict[letter] + " ")

