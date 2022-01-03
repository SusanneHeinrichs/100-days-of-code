
import pandas

data = pandas.read_csv("/Users/suse/dev/100-days-of-code/Day30/NATO+Phonetic+Alphabet+for+the+Code+Exercise/nato_phonetic_alphabet.csv")
# #TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word:").upper()
    try: 
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error_message:
        print(f"You typed in {error_message}, but only letters of the alphabet are allowed. ") 
        #generate_phonetic()
    else:
        print(output_list) 
 

generate_phonetic()
