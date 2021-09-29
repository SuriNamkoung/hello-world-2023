# This code is for kids. very easy and simple HaHa

# An object describing our player
player = {
    "name": "p1"
}


def printGraphic(name):
    if (name == "title"):
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~')
        print (' WELCOME TO THE SAFARI')
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~')
        print ('                         ')
        print (' __         __')
        print ('/  \.-"""-./  ')
        print ('\    -   -    /')
        print (' |   o   o   |')
        print ('  "-\__Y__/-"')
        print ('     `---`')
    
    if (name == "fox"):
        print ('   /\   /\            ')
        print ('  // \_// \     ____  ')
        print ('  \_     _/    /   /  ')
        print ('   / * * \    /^^^]   ')
        print ('   \_\O/_/    [   ]   ')
        print ('    /   \_    [   /   ')
        print ('    \     \_  /  /    ')
        print ('     [ [ /  \/ _/     ')
        print ('    _[ [ \  /_/       ')
        print ('                      ')


    if (name == "owl"):
        print ('────▐──▌─────▐──▌────')
        print ('───▐▌─█───────█─▐▌───')
        print ('──▄█──▀▀▄▌▄▐▄▀▀──█▄──')
        print ('─▐█─▄█▀▄█████▄▀█▄─█▌─')
        print ('──▀▀─▄▄▄█████▄▄▄─▀▀──')
        print ('───▄█▀─▄▀███▀▄─▀█▄───')
        print ('─▄█──▄▀──███──▀▄──█▄─')
        print ('▐█───█───▐█▌───█───█▌')
        print ('─█────█───▀───█────█─')
        print ('─▀█───█───────█───█▀─')
        print ('──█────█─────█────█──')
        print ('───█───█─────█───█───')
        print ('────▌───▌───▐───▐────')



def introStory():
    # let's introduce them to our world
    print ("Hi, there. You will go a safari with me. What is your name?")
    player["name"] = input("Please enter your name> ")
    print ("")

    print ( player["name"] + "," + " There are two different types of species we can see.")
    print ("Which ways do you want to go.") 

    pcmd = input("Choose: (1) Green forest OR (2) Dark cave> ")
    print("")

    # the player can choose 1 or 2
    if (pcmd == "1"):
        path1()

    elif (pcmd == "2"):
        print ("You're really fearless.")
        print(input("Press enter>"))
        path1()

    else: 
        path1()

def path1():
    print ("We are arrived at a certain mountain.")
    print ("there are some foods you can give to some animals")
    print (input("Press enter>"))

    import random
    myList = ["Kimchi", "potato", "carrot", "New York pizza"]
    print("You've been recieved: " + random.choice(myList) + "!" )
    print (input("Press enter>"))

    print("The food you have is really healthy for 00")

    # the player chooses 1 or 2
    pcmd1 = input("(1) mammal (2) bird>")

    print ("")

    if (pcmd1 == "1"):
        print("Something is moving behind the forest.")
        print("Should we go closer?.")
        print(input("Press enter>"))

        printGraphic("fox")
        print("")
        print("What a cute fox it is!!")

    elif (pcmd1 == "2"):
        print("It's a really dark night.")
        print("Crunching, rustling.")
        print (input("Press enter>"))

        printGraphic("owl")
        print("You finally found the owl!")
        print("They are nocturnal animals like me doing assignments late at night ")


# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens