import random


top_of_range= input('Input a number :')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range<=0:
        print('pls input number larger than 0')
        quit()
else :
    print("Please Input a number ONLY")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

print(random_number)

while True:
    guesses +=1
    user_guess = input("make a guess : ")
    if user_guess.isdigit():
             user_guess = int(user_guess)

    
    else :
                print("Please Input a number ONLY")
                continue

    if user_guess == random_number:
        print("You got it")
        break
   
    elif user_guess> random_number:
            print("You are above the number")
    else:
            print('you are lower the number')


print('You got it in ', guesses,' guesses' )