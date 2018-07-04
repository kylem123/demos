 #v2 changelog
#Added reel checking logic

import re
import random

balance_format = "[0-9][0-9].[0-9][0-9]"

fruits = ["Apple", "Banana", "Lemon", "Cherry", "Mango"]

reels = [0, 0, 0]

initial_balance = 0
balance = 0
winnings = 0
jackpot = 0

def spin():
    global balance, jackpot
    balance -= 0.50 #Subtract 50p
    jackpot += 0.50 #Add to the jackpot
    for i in range(len(reels)):
        reels[i] = random.randint(0, len(fruits) - 1)
        
    print("++++++++++++++++++++++++++")
    print("+ " + fruits[reels[0]] + " | " + fruits[reels[1]] + " | " + fruits[reels[2]] + " +")
    print("++++++++++++++++++++++++++")
def check_reels():
    global initial_balance, winnings, jackpot # <- I used the global keyword in several cases as I was getting errors about the variables not being defined

    prize = 0
    
    if(reels[0] == reels[1] and reels[0] == reels[2]): #All 3 are the same
        if(fruits[reels[0]] == "Cherry"): #If all 3 are cherries
            print("JACKPOT!")
            prize += jackpot
            jackpot = 0
        else:
            prize += 10
    elif(reels[0] == reels[1]):
        prize += 5

    if(fruits[reels[2]] == "Cherry"): #Check if it is a cherry on the last reel
        prize += 1

    winnings += prize
    profit = winnings - initial_balance
    pos_profit = str(profit)[1:] #Substring to remove -
    print("You have won £" + str(prize) + "! Your total winnings are now £" + str(winnings) + " and your profit is " + str("-£" + str(pos_profit) if profit < 0 else "£" + str(profit)) + "!")
        

def main():
    print("~~Fruit Machine By Kyle Mandell~~")
    x = 0
    x = input("(One spin costs 50p | Minimum spend of £1 | Press ENTER to pull the lever and spin!)\nHow much money do you have? £")
    while(float(x) < 1):
        x = input("LESS THAN MINIMUM SPEND! (One spin costs 50p | Minimum spend of £1 | Press ENTER to pull the lever and spin!)\nHow much money do you have? £")
        
    global initial_balance, balance, jackpot
    initial_balance = int(x)
    balance = initial_balance

    print("")
    while(balance >= 0.50): #Loop whilst there is enough money
        spin()
        check_reels()

        #loaded_jackpot = open("Jackpot.txt", "r").read()

        #file = open("Jackpot.txt", "w") # <- Writing to file isn't working completely yet (Needs to add new total to old total)
        #file.write(str(jackpot))

        #file = open("Jackpot.txt", "r")
        
        print("You have £" + str(balance) + "0" + " left and the jackpot is now £" + str(jackpot) + "0")

        input("")

    print("Game Over!")
    profit = winnings - initial_balance
    pos_profit = str(profit)[1:] #Substring to remove -
    print("Your total winnings were £" + str(winnings) + " and your profit is " + str("-£" + str(pos_profit) + " :(" if profit < 0 else "£" + str(profit) + " :)")) # <- Ternary Operators 
    
main()
