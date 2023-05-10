#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

"""
Mail Merge project, the program takes a list of names and inserts them into a letter templates
and outputs it into specially named files
"""

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letter_temp = file.read()

for name in names:
    name = name.strip()
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(letter_temp.replace("[name]", name))

