#Step 1 importing modules
import random 
import hangman_art
import hangman_words

#get a random word
randomWord=random.choice(hangman_words.word_list)
randomWordLength=len(randomWord)

#lives
lives=6

#hangman logo
print(hangman_art.logo)


#creating an empty list
display=[]
for countLetters in range (0,randomWordLength):
  display.append("_")

#initially end of game is False
game_end=False

#asking user input until display get filled
while not game_end:

  # guessing a letter
  guess=input("Guess a letter: ").lower()

  
  #informing user if word has been guesses
  if guess in display:
    print(f"You have already guessed {guess}")

  #checking if user input matches with letter
  for letterIndex in range(randomWordLength):
      letter=randomWord[letterIndex]
      if guess==letter:
        display[letterIndex]=letter
  
  if guess not in randomWord:
    lives-=1
    print(f"{guess} is not there in the Word! You lose one life! Total lives={lives}(6)\n")
    if lives==0:
      game_end=True
      print("You Lose the Game !")
      print(f"The correct word is {randomWord}")
      

  #printing the display
  print(display)

  if "_" not in display:
    game_end=True
    print("YOU WIN THE GAME !")

  print(hangman_art.stages[lives])



