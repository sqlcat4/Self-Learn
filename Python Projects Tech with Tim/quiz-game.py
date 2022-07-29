print("Welcome to my Computer Quiz")

playing =input("Do you want to play? ")

if playing.lower() != "yes":
            quit()

print("Okay! Lets play : ) ")
score = 0

answer = input("What Does CPU Stand For?  ")

if answer.lower()  == "central processing unit":
                print('correct')
                score+=1
else: 
        print('incorrect')
        
        
answer = input("What Does GPU Stand For?  ")

if answer.lower()  == "graphic processing unit":
                print('correct')
                score+=1

else: 
        print('incorrect')

answer = input("What Does RAM Stand For?  ")

if answer.lower()  == "random access memory":
                print('correct')
                score+=1

else: 
        print('incorrect')

answer = input("What Does PSU Stand For?  ")

if answer.lower()  == "power supply unit":
                print('correct')
                score+=1

else: 
        print('incorrect')


print("You got " + str(score) + " questions correct !")
print("You got " + str((score/4) * 100) + " % score!")
