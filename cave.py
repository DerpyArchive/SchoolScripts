print ("Welcome to the Dark Cave Game by MEEEEEE. Type a number when the program asks you to do so if you want to do stuff (╯◕ヮ◕）╯︵ ┻━┻")
print ("You enter a dark cave, on the mountain. The cave has a corridor with two doors at the end of it.  Do you go through door number 1 or door number 2, or try to exit the cave(3)?")

door = input("> ")

if door == "1":
    print ("Hmm..you went through the door and there is a massive cliff opening out to a sandy beach. What do you do?")
    print ("1. Jump off it.")
    print ("2. Go back")
    print ("3. Try and climb down")
	
if door == "2":
    print ("There was nothing in there.")
    print ("You go back, but the door locked behind you. You waited, but eventually you died of hunger. R.I.P")
    print ("That is the end of the game. I hope you enjoyed ツ")

if door == "3":
    print ("You tried to go back, but a rock had fallen down and you can't get out.")
    print ("You try to open the doors, but they are all locked. You waited, but eventually you died of hunger. R.I.P")
    print ("That is the end of the game. I hope you enjoyed ツ")    
    
cliff = input("> ")
	
if cliff == "1":
        print ("You jumped off the cliff and died. R.I.P")
        print ("That is the end of the game. I hope you enjoyed ツ")
        
elif cliff == "2":
        print ("You tried to go back to the cliff, but the door was locked. You fell off the cliff and died. R.I.P")
        print ("That is the end of the game. I hope you enjoyed ツ")

elif cliff == "3":
        print ("You tried to climb down, but slipped on a rock. You fell off the cliff and died. R.I.P")
        print ("That is the end of the game. I hope you enjoyed ツ")        
