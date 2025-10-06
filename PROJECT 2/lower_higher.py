#generate random guess range and generating a random number within the range
import random

def ran_range():
    a=random.randint(1,90)
    rng=f"{a} to {a+10}"
    guess=random.randint(a,(a+10))
    print("The number is in the range",rng)
    return guess,a

def help():
    print("\n========== HELP MENU ==========")
    print("1. A random range of numbers will be generated (e.g., 25 to 35).")
    print("2. A secret number will be chosen inside that range.")
    print("3. Your job is to guess the number!")
    print("4. After each guess, you'll get a hint:")
    print("   - 'HIGHER!!' means the secret number is bigger.")
    print("   - 'LOWER!!' means the secret number is smaller.")
    print("5. Keep guessing until you find the correct number.")
    print("6. At the end, you'll see how many guesses you took.")
    print("================================\n")
    rerun=input("So wanna start the game now?(Y/N): ")
    if (rerun=="Y"):
        run()       
    else:
        print("Thanks for playing!") 

#main stucture generating a number
def logic(guess,a):
    user=int(input("Enter your number: "))
    i=0
    while(user != guess):
        if(user<guess):
            print("HIGHER!!")
        elif(user>guess):
            print("LOWER!!")
        user=int(input("Enter your number: "))
        i+=1
    i+=1
    print(f"You Guessed Right!!!\nNumber of guesses: {i}")
    


#guess system
def run():
    print("Welcome to the RANDOM NUMBER GUESSER!!\n For Rules Enter 'help'\nTo start the game Enter 'start'")
    option=input("Enter your option: ")
    guess,a=ran_range()
    if(option=="help"):
        help()
    else:
        
        logic(guess,a)
run()
