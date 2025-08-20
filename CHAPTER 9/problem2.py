#set high score
import random
def game():
    print("You are playing a game")
    score=random.randint(1,89)
    with open("CHAPTER 9/hiscore.txt") as f:
        hiscore= f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score: {score}")
    if(score>hiscore):
        with open("CHAPTER 9/hiscore.txt","w") as f:
            f.write(str(score))
            print(f"New High-score: {score}")

    return score

game()