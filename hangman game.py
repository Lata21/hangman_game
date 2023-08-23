#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Implemnetation of hangman game:-


# In[2]:


import random
import os

# Words and stages
words_list = ["affix", "avenue", "awkward", "beekeeper", "boggle", "cobweb", "cycle", "disavow", "duplex", "equip",
              "exodus", "funny", "galaxy", "gossip", "icebox", "injury", "ivory", "jackpot", "jelly", "jockey",
              "joking", "joyful", "jumbo", "kayak", "khaki", "kiosk", "lengths", "lucky", "luxury", "lymph",
              "nightclub", "onyx", "over", "pajama", "pneumonia", "pshaw", "puppy", "scratch", "staff", "stretch"]

stages = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

def select_word_by_length(length):
    filtered_words = [word for word in words_list if len(word) == length]
    return random.choice(filtered_words)

# Choose the word length you want to guess
word_length = random.choice([5, 6])  # You can set this to 5 or 6

choice_word = select_word_by_length(word_length)

display = ['_'] * len(choice_word)
lives = len(stages)

while lives > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    found = False
    for position in range(len(choice_word)):
        letter = choice_word[position]
        if letter == guess:
            display[position] = guess
            found = True

    if not found:
        lives -= 1
        print(stages[lives])

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print(" ".join(display))

if '_' not in display:
    print("Congratulations! You win! The word was:", choice_word)
else:
    print("Sorry! You lose. The word was:", choice_word)


# In[ ]:




