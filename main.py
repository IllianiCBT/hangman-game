import random


def menu():
    checked = 0
    selection = ""

    while checked == 0:  # check player has selected one of the three viable options and if not, prompt for re-entry
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

        viable_selections = ["play", "results", "exit"]
        selection = input()

        if selection in viable_selections:
            checked = 1

    if selection == "play":
        game()
    elif selection == "results":
        scoreboard()
    elif selection == "exit":
        quit()


def scoreboard(add_win, add_loss):
    wins = 0
    loses = 0
    print(f"You won: {wins} times.")
    print(f"You lost: {loses} times.")


def generate_answer():  # randomly select a word from the available list & mask it
    library = ["python", "java", "swift", "javascript"]

    answer = random.choice(library)  # randomly select word from available list
    answer_list = list(answer)  # convert word into a list of characters

    mask_answer = "-" * len(answer)  # determine length of mask
    masked_list = list(mask_answer)  # convert mask into a list

    return answer, answer_list, masked_list


def guess_checker(masked_list):  # check guess is valid
    print("Input a letter:")

    guess = input()
    guess_checked = 0

    while guess_checked != 1:
        if len(guess) == 0:
            print("Please, input a single letter.")
            print(''.join(masked_list))  # display masked list with mask replaced by all instances of guessed letter

            print("Input a letter:")
        if len(guess) > 1:
            print("Please, input a single letter.")
            print(''.join(masked_list))  # display masked list with mask replaced by all instances of guessed letter

            print("Input a letter:")
            guess = input()
        elif guess.isalpha() is False or guess.islower() is False:
            print("Please, enter a lowercase letter from the English alphabet.")
            print(''.join(masked_list))  # display masked list with mask replaced by all instances of guessed letter

            print("Input a letter:")
            guess = input()

        else:
            guess_checked = 1

    return guess


def attempt_answer(answer_list, masked_list, attempts):
    previous_answers = []
    while attempts > 0:
        guess = guess_checker(masked_list)  # the player selects a letter to check against the answer

        if guess in previous_answers:
            print("You've already guessed this letter")
            print(''.join(masked_list))  # display existing masked list
        elif guess not in answer_list:
            attempts -= 1
            print(f"That letter doesn't appear in the word.  # {attempts} attempts")
            print(''.join(masked_list))  # display existing masked list
            previous_answers.append(guess) # add to list of previous guesses
        else:
            previous_answers.append(guess) # add to list of previous guesses

            index = -1

            for letter in answer_list:
                index += 1
                if letter == guess:
                    masked_list[index] = guess  # replace mask with all correctly guessed letter
            print(''.join(masked_list))  # display masked list with mask replaced by all instances of guessed letter

        if ''.join(masked_list) == ''.join(answer_list):  # check to see if game has been won
            print(f"You guessed the word {''.join(answer_list)}!")
            print("You survived!")
            break
        elif attempts < 1:  # if the game hasn't been won, check to see if it has been lost
            print("You lost!")


def game():
    # SETTINGS
    chosen_word, letters, mask = generate_answer()  # select a word from a predefined library & mask it
    attempts = 8

    print(''.join(mask))  # display masked word

    attempt_answer(letters, mask, attempts)  # user attempts to guess letters in word until out of attempts

    menu()


if __name__ == '__main__':
    print(f"H A N G M A N  # 8 attempts")  # game title

    menu()
