''' 
    Name: Snowball-Mania
    Author: Jalyn Jarboe    
    Date: 12/3/2024
    Class: AP Computer Science Principles
    Python: 3.11.5
'''
import random
import time
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def __new__(self):
        name = ""
        health = 100
def main():
    
    # the main runner of the game
	# welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name = input("What is your name?   ")
    opponent = input("Great to have you here, " + name + "! Who do you want to play against?   ")
    print(name.capitalize() + ' vs. ' + opponent.capitalize())

    players = []
    players.append(name)
    players.append(opponent)

    nextPlayer = ""
    while nextPlayer != "DONE":
        nextPlayer = input("Are there any other opponents? If so, type them one at a time (or DONE) and press 'Enter'   ")
        players.append(nextPlayer)
    players.remove("DONE")

    choice = input("Do you want to play on Manual mode? (Type YES or NO)   ")

    gamePlay(name, players, choice)

   # randomly choose one person to throw a snowball at the other
    

def gamePlay(name, players, manual):
    while len(players) > 1:
        thrower = random.choice(players)
        if thrower == name:
            if manual == "YES":
                print("***Player***")
                for i in players:
                    if i != name:
                        print(i)
                target = input("You are throwing! Who from the list above do you want to throw a snowball at?   ")
                while target == thrower:
                    target = input("You can't throw snowballs at yourself!? Who else do you want to throw at?   ")
                
            else:
                target = random.choice(players)
                while target == thrower:
                    target = random.choice(players)

        else:
                target = random.choice(players)
                while target == thrower:
                    target = random.choice(players)
                # print(target)
        print(f'{thrower} is throwing a snowball at {target}!')
    
        # generate random number to use as the hitNum
        hitNum = random.randint(1,5)
        success = hitResult(hitNum)
        if success == True:
            print(f"It's a hit! {target} is down!")
            players.remove(target)
        else:
            print(f"Unfortunately, {thrower} is kinda bad, and missed.")
        time.sleep(1)

    print(f'{players[0]} is the best snowball fighter of all!')


def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    if hitNum == 5:
        return True
    return False
    # indicating if this was a hit or a miss
    return false

main()
