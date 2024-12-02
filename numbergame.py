import random
import os

secret_num = 0
range = []
guess_left = 0
guess_made = 0
guess = 0
hint = ''
print ('\t\t\tGuess the Number!\t\t\t\n' +
        'Choose Dificulty:\n'+
        'Range 1 - 10 \t[1]\n'+
        'Range 1 - 50 \t[2]\n'+
        'Range 1 - 100 \t[3]')

diff = input("Enter the number of chosen difficulty:")
flag = True

# NUMBER RANDOMIZER
match diff:
    case '1':
        range = [1,10]
        secret_num = random.randint(1,10)
        guess_left = 3
    case '2':
        range = [1,50]
        secret_num = random.randint(1,50)
        guess_left = 4
    case '3':
        range = [1,100]
        secret_num = random.randint(1,100)
        guess_left = 5
    case _:
        flag = False
        secret_num = random.randint(1,10)

# CLEAR TERMINAL
os.system('cls||clear')

if (not flag):
    diff = 1

# GAME LOGIC
while (guess_left != 0 and guess != secret_num) :
    ans = secret_num    
    print ('\t\t\tGuess the Number!\n' +
        '\t\t   Proceeding to difficulty [' + diff + ']\n' +
        f'\t\t\t  Range {range}\n\n\n')
    
    print (f'Guesses Left: {guess_left}')
    print (hint)

    print (ans)
    guess = int(input('Enter Your Guess: '))

    if (guess < ans):
        hint = 'HIGHER!'

    if (guess > ans):
        hint = 'LOWER!'
    
    guess_left -= 1
    guess_made += 1
    os.system('cls||clear')

# CLEAR TERMINAL
os.system('cls||clear')

if guess_left != 0 or guess == secret_num:
    print (f'YOU GOT IT RIGHT WITH {guess_made} GUESSES!')
else:
    print ('You ran out of guesses!\n' +
           'Better Luck Next time!')
    



