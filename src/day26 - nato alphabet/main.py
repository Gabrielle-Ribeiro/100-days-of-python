import pandas as pd

alphabet_df = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_dictinary = {row.letter:row.code for index, row in alphabet_df.iterrows()}

user_input = input().upper()
phonetic_code = [phonetic_dictinary[letter] for letter in user_input]

print(phonetic_code)