import random

options=["k","l",'n']
while True:
    user_input=input('Input :').lower()

    if user_input == 'q':
        break

    if user_input  in options:
        print('correct')
        continue