print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("You're in the middle of the jungle. You walked and found a crossroad.")
first_choice = input('Which direction do you wanna go? Type "left" or "right": ').lower()
print("\n")


if first_choice == "left":

    print("You've come to a lake. There is an island in the middle of the lake.")
    second_choice = input('What do you wanna do? Type "swim" to swim across or "wait" to wait for a boat: ').lower()
    print("\n")

    if second_choice == "wait":

        print("You arrive at the island unharmed. There is a house with three doors. Which door do you choose?")
        third_choice = input('Type "red" for the red one. Type "blue" for the blue one. Or type "yellow" for the yellow one? ').lower()
        print("\n")
        
        if third_choice == "red":
            print("You are in hell. You died burned by fire. Game over!!")
        elif third_choice == "blue":
            print("Bad choice. You were eaten by beasts. Game over!!")
        elif third_choice == "yellow":
            print("Congratulations! You found the treasure. You win!!!")
        else:
            print("Wrong choice! Game over!!")

    else:
        print("You were attacked by a giant trout. Game over!!")

else:
    print("Bad choice. You fell into a hole. Game over!!")