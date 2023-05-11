"""
NATO Alphabet, the user enters a word and the program prints a list of the NATO Phonetic Alphabet spelling
"""
import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

word = input("Enter a Word: ").upper()

nato_list = [alphabet[letter] for letter in word]

print(nato_list)
