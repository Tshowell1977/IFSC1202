from random import randint

name=input("Hello! What is your name?")

print("Well,",name,", I am thinking of a number between 1 and 20.")
print(" You have five guesses.")

x = randint(1,20)

ct=1
for i in range(1,6):
    n = int(input("Take a guess:"))  
    if n ==x:
        print("Good job,",name,"! You guessed my number in",ct," guesses!")
        break
    if n <x:
        print("Your guess is too low.")
    if n >x:
        print("Your guess is too high.")
    ct+=1
print ("Nope. The number I was thinking of was ",ct)