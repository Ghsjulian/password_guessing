# importing random
import os
import color 
from random import *
import random as rnd

os.system("clear")

os.system('figlet -f small "GHS JULIAN"|lolcat\n')


# taking input from user
user_pass = input(color.BOLD+color.YELLOW+color.BOLD+"\n   [+] Enter Your Password :  "+color.LIGHT_CYAN)

password = ""
guess = ""
algorithm = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', ]

def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

while (user_pass):
  try:
   file = open("10-million-password-list.txt", 'r')
   paswd = file.readlines()
   for words in paswd:
      final_pass = words.strip()
      password = final_pass
      #word = Convert(password)
      if user_pass == password:
        guess = password 
        os.system('clear && \n\nfiglet -f small "GHS JULIAN"|lolcat\n')
        print (color.BOLD+'''       Congratulations Password Found !      \n'''+color.BOLD+color.YELLOW+'''

 +----------------------------------------------+'''+color.BOLD+color.BLUE+'''
 |                                              |
 |                                              |
'''+color.BOLD+color.RED+''' |         Your Password : '''+color.BOLD+color.LIGHT_GREEN+password+'''              |
 |                                              |
'''+color.BOLD+color.GREEN+''' +----------------------------------------------+
''')

        user_pass = False
        break 
      print(rnd.choice(color.color_list)+"\n\n   Gussing Your Password ---->>  "+color.YELLOW+color.BOLD+password)
      if password == "finished":
        user_pass = False
        print(rnd.choice(color.color_list)+"\n\n  ______Password Not Found_______  ")
  except Exception:
    raise Exception



