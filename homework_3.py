
# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
name = raw_input("what is your name: ")
schoolname = raw_input("What is your school's name?: ")
classname = raw_input("What is your least favorite class: ")
friend = raw_input("A classmate comes to your mind who has different sex with you: ")
adjective = raw_input("I like a person who is so 000(adjective): ")
Classmate = raw_input("Enter one classmate comes to your mind: ")
occupation = raw_input("Enter what do you want to become: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "Hi, my name is " + name + " I am a student at " + schoolname + " My favorite class in Fall semester is " + classname + ". " \
"I want to go to a famous restaurant in NewYork with " + friend + " Because he or she is so " + adjective + ". " \
"I want to do the group project with " + Classmate + " . " \
"Oneday I strongly believe I can be a good " + occupation + " after graduating the school. "

# finally we print the story
print (story)