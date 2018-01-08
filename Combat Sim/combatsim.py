# This will simulate a round of combat between you and a goblin.
import random
import time
goblinHP = "10"
yourHP = "15"
#define the combatRND function.
def combatRND():
    global goblinHP
    goblinAC = 10
    global yourHP
    yourAC = 12
    rollDMGgoblin  = random.randint(1,6)
    rollDMGyou = random.randint(1,6)
    print("The goblin has ",  goblinHP,  "health")
    print("You have ",  yourHP,  "health")
    time.sleep(1)

    gobboAttack = random.randint(1,20)
    if gobboAttack > yourAC:
        rollDMGgoblin = str(rollDMGgoblin)
        yourHP = str(yourHP)
        time.sleep(2)
        print("The goblin hit you for ",  rollDMGgoblin,  "!")
        yourHP = int(yourHP)
        rollDMGgoblin = int(rollDMGgoblin)
        yourHP = yourHP - rollDMGgoblin
        time.sleep(2)
        print("Your HP is now ", + yourHP)
    else:
        time.sleep(2)
        print("The goblin missed!")

    yourATK = random.randint(1,20)
    if yourATK > goblinAC:
            rollDMGyou = str(rollDMGyou)
            goblinHP =  str(goblinHP)
            time.sleep(2)
            print("You hit the goblin for ",  rollDMGyou,  "!")
            goblinHP = int(goblinHP)
            rollDMGyou =  int(rollDMGyou)
            goblinHP = goblinHP - rollDMGyou
            time.sleep(2)
            print("The goblin's health is now ", + goblinHP)
    else:
            time.sleep(2)
            print("Your attack missed!")



print("what's your character's name?")
myName = input()
print("Look out! " + myName + ", a goblin leaps from the cave and lunges at you, trying to kill you!")
print("Type 'a' to defend yourself!")
command = input()
if command == "a":
    combatRND()
else:
    print("You failed to defend yourself and the goblin makes a meal of you!")
    quit()

while int(goblinHP) > 0 and int(yourHP) > 0:
    combatRND()
if int(yourHP) <= 0:
    print('As your vision fades to darkness, the last thing you see is the goblins grinning maw!')
if int(goblinHP) <= 0 :
    print("Congratulations! " + myName +" You have defeated the goblin!")

















#print("Well, " + myName + ",I am thinking of a number between 1 and 20.")

#for guessesTaken in range(6):
#    print("Take a guess!")
#    guess =  input()
#    guess = int(guess)

#    if guess < number:
    #    print("Your guess is too low.")

#    if guess > number:
#        print("Your guess is too high.")

#    if guess == number:
#        break

#if guess == number:
#    guessesTaken = str(guessesTaken + 1)
#    print("Good job, " + myName + "! You guessed my number in " + guessesTaken + " tries!" )

#if guess != number:
#    number = str(number)
#    print("Nope. The number I was thinking of was " + number + ".")
