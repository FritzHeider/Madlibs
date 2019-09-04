
print ("Hello! Welcome to Mad Fritz's Lib Game!")
print ("In order to play the game i need you to input some parts of speech for me")


#maybe best to bunch uop the types of speech so the can be entered in faster
verb0 = input("First we need four verbs starting with a regular verb> ")
verb1 = input("please enter a plural verb > ")
verb2 = input("enter an action verb for me > ")
verbs3 = input("enter one last action verb for me > ")

#if i had time i know i should really be creating all these as lists so i can randomize them
#baby steps to the door i learned a whole lot from this exercise and really just realized how much mnore i have to learn
nouns0 = input("enter a plural noun here >  ")
nouns1 = input("And a regular noun > ")
nouns2 = input("enter a plural noun > ")
nouns3 = input("enter a body part >  ")
nouns4 = input("enter a plural noun > ")

adjec0 = input("Alright and we are almost done, enter one adjective place > ")
adjec2 = input("and last one! enter another adjective > ")

#i know i could do so much bertter with the formatting
def story():
    print ('''



    ''')

    print ("The day I saw the Monkey King I " + verb0 + " It was one of the most interesting days of the year.")

    print ("\nI still cannot believe my " + nouns0 + " I had the " + verb1 + " running through my body for over a week.")

    print ("\nThe Monkey King is one of the largest " + nouns1 + " I had seen in person. The funniest thing was when he" + adjec0)

    print ("\n" + verb2 + "in a huge pile of " + nouns2 + " After he did that he played chess on his brothers" + nouns3 )

    print ("\nand combed his " + adjec2 + " hair with a comb made out of fish bones")

    print ("\nLater that same day, i saw the monkey king" + verbs3 + " in front of an audience of" + nouns4)

print(story())
