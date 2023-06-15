import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
choosen_word=random.choice(word_list)
length=len(choosen_word)
lives=length
display=[]
for letter in choosen_word:
        display.append("_")
end_of_game=False
while end_of_game==False and lives>0:
    guess=input("Enter a letter which you think is in this word ")
    guess=guess.lower()
    for i in range(length):
        for letter in choosen_word[i]:
            if guess==letter:
                display[i]=letter
    if guess not in choosen_word:
        lives-=1
        print("You have guessed",guess,"but it is not in the word. Sorry but you lose a life")
        print("You have",lives,"lives left")
    print(display)
    if '_' not in display:
        end_of_game=True
        print("You Win")
    if lives==0:
        print("You Lose")
    print(stages[lives])
    
