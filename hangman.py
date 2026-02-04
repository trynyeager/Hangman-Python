import random
import os
import time

hangman_assets = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

animal_names = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def blankD(blanks): # to display the blanks
    for i in blanks:
          print(i+" ",end="")    
    print()

def hangs(i):
    print(hangman_assets[i])

rt = "\u001b[0m" #plain
g = "\u001b[32m" #grn
b = "\u001b[34m"
r = "\u001b[31m" #red

chance = 7

def display(blanks,comp_choice):
   os.system('cls')
   print("Hangman - by Tryn\n")
   print("Theme : Animals\n\nTotal Chances : 6")
   print(f"Wrong guesses : {7-chance}")
   if hint:
      print(f"\nWord is {comp_choice}\n")
   hangs(7-chance)
   blankD(blanks)  

def game(): #main game function
    
    global chance #global variables
    global hint
    global running

    hint=False
    running=True
    comp_choice = animal_names[random.randint(0,len(animal_names)-1)] #pick the random word
    blanks = '_'*len(comp_choice)
    blanks = list(blanks)
    Tcomp_choice=list(comp_choice) #splits the word into array elements
    correct_guess=0 #handles correct guesses

    while chance!=0 and running: #chances counter 

      display(blanks,comp_choice) #displays game menu
      user_choice = input("\nEnter an Alphabet: ").lower() #accepts user choice
      found=False #check for correct word guess
      i=0 #for repeated words
      if user_choice == "cheat":
        hint=True
      if user_choice == "win":
        print(f"{r}bruh cheater :/{rt}") #this took a very long time to handle, it was repeating itself on a loop idk how
        running=False
        continue
        # chance=10

      for j in range(len(Tcomp_choice)):
        
        if user_choice == Tcomp_choice[j]: # correct guess handler
            repeat=False
            for x in range(len(blanks)):
              if user_choice==blanks[x]:
                  if repeat: print(f"{g}Already Guessed!{rt}")
                  repeat=True
                  i+=1
                  time.sleep(1) if not repeat else None
            # if not repeat:
            i+=1
            if i==1 and not repeat:
              print(f"{g}Correct guess!{rt}")
              time.sleep(1)
            # if not repeat:
            correct_guess+=1
            blanks[j] = user_choice
            found=True
      if not found and user_choice != "cheat" and user_choice != "win": #cheat code and wrong guess handler
          # if user_choice == "cheat":
            #  print(f"{r}bruh ._.{rt}") #dont cheat
          # else:
          print(f"{r}Wrong guess!{rt}")
          time.sleep(1)
          # wrong+=1
          chance-=1
      if correct_guess == len(comp_choice): #game won
        display(blanks,comp_choice)
        # blankD(blanks)
        print(f"\n{g}Guessed Correctly!{rt}")
        running=False
      if chance == 1: #terminate the game
         display(blanks,comp_choice)
         print(f"\n{r}Chances over! The correct word was{rt}",comp_choice.capitalize())
         running=False
      
if __name__ == "__main__":
    game()