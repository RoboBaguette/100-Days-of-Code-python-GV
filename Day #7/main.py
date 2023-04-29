import random
import word_l
import art

# start screen
print(art.logo)
print("Walcome to hangman.")
# word generation
word_c = word_l.word_list[random.randint(0, 213)]
word_len = len(word_c)
# word clue # of letters
print(f"the number of letters in the word is {word_len} \n")
word_dash = []
for n in range(0, word_len):
    word_dash += "-"
print(f"{''.join(word_dash)}")
# game loop
num_right = 0
num_wrong = -1
word_dash2 = ""
while num_right != word_len:
    letter = input("Guess a letter: ")
    if letter in word_dash:
        print(f"You have already guessed the letter {letter}.")
    else:
        if letter in word_c:
            num_right += word_c.count(letter)
            a = word_c.count(letter)
            print(f"Correct, the letter {letter} is in the word {a} times.\n")
            pos = []
            for num in range(0, word_len):
                if letter == word_c[num]:
                    pos.append(num)
            for n in range(0, a):
                word_dash[pos[n]] = letter
            print(f"{''.join(word_dash)}")
            print("\n\n")
            print(art.stages[num_wrong])
        else:
            num_wrong -= 1
            print(f"Wrong the letter {letter} is not in the word\n")
            print(f"{''.join(word_dash)}")
            print(art.stages[num_wrong])
        if num_wrong == -7:
            print("You have failed.\nGAME OVER")
            break
        if num_right == word_len:
            print("You win!\nGAME END")

