import random

num_digits= 3
max_guesses= 10

def main():
    print('''\nI'm thinking of a {} digit number with no repeated numbers.
        \nTry to guess what it is with some clues:
        When I say:     What I mean:
        Pico            One digit is correct but in the wrong position.
        Fermi           One digit is correct and in the right position.
        Bagels          No digit is correct.'''.format(num_digits))

    while True:
        # stores  value that player has to guess
        secret_numb = get_secret_numb()
        print(secret_numb)
        print('You have to guess a {} guesses.'.format(max_guesses))

        num_guesses = 1
        while num_guesses<= max_guesses:
            guess=''
            # prompt until the user inputs a valid guess
            while len(guess) != num_digits or not guess.isdecimal():
                guess= input( 'guess #{}: '.format(num_guesses))
                if len(guess) != num_digits:
                    print(f"Please enter a {num_digits}-digit number.")

            clues = get_clues(guess, secret_numb)    ##wether guess == secret_num
            print(clues)
            num_guesses+=1


            # condition for game over and re-run
            if guess == secret_numb:
                print('congrats you guessed it!')
                break
            if num_guesses > max_guesses:
                print('oops, you ran out of guesses.')
                print('the secret number was {}'.format(secret_numb))

        print('would you like to play again? (yes/no)')
        if not input('< ').lower().startswith('y'):
                break
    print('thanks for playing!')


#returns string of unique random digits
def get_secret_numb():
    numbers=list('0123456789')
    random.shuffle(numbers) # Shuffle them into random order.

    secret_numb=''
    for i in range(num_digits):
        secret_numb += str(numbers[i])
    return secret_numb

def get_clues(guess, secret_numb):
    if guess == secret_numb:
        return 'you got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_numb[i]:  # Correct digit in correct position
            clues.append('Fermi')
        elif guess[i] in secret_numb:  # Correct digit, wrong position
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'  # No correct digits at all
    else:
        clues.sort()
        return '  '.join(clues)


if __name__ == '__main__':
    main()


