# short program to determine letter colors for word guess
# my current challenge is incorporating this into the def check.letters(self):

import os
def clear_console():
  os.system('cls')

clear_console()

while True:

  print()
  print('  Enter secret word : ', end='')
  secret_word = input()
  secret_word = secret_word.upper()
  
  if secret_word == '':
    print()
    print('  Exiting')
    break
  else: 
    print('  Enter guess word  : ', end='')
    guess_word= input()
    guess_word = guess_word.upper()

    #determine number of occurences of each letter
    guess_occurs = ''
    secret_occurs = ''
    for i in range(5):
      guess_num = 0
      secret_num = 0
      for j in range(5):
        if guess_word[i] == guess_word[j]:
          guess_num += 1
        if secret_word[i] == secret_word[j]:
          secret_num += 1
      guess_occurs = guess_occurs + str(guess_num)
      secret_occurs = secret_occurs + str(secret_num)

    word_colors = ''
    for i in range(5):
      if guess_word[i] == secret_word[i]:
        word_colors = word_colors + 'G'
      elif guess_word[i] in secret_word:
        if int(guess_occurs[i]) >  int(secret_occurs[i]):
          word_colors = word_colors + 'B'
        else: 
          word_colors = word_colors + 'Y'
      else:
        word_colors = word_colors + 'B'

    print()
    print('  secret word  :', secret_word)
    print('  guess word   :', guess_word)
    print('      colors   :', word_colors)
    print()
    print('  secret occurs:', secret_occurs)
    print('  guess occurs :', guess_occurs)
    print()






