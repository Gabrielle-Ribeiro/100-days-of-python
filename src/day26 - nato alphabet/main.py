import pandas as pd

alphabet_df = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_dictinary = {row.letter:row.code for index, row in alphabet_df.iterrows()}

phonetic_code = ""
while len(phonetic_code) == 0:
    user_input = input().upper()
    try:
        phonetic_code = [phonetic_dictinary[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")

print(phonetic_code)