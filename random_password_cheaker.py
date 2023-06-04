# importing libraries 
import color
import os,sys,time
import random as rnd
from random import *
def _load(z):
  for e in z + '\n':
     sys.stdout.write(e)
     sys.stdout.flush()
     time.sleep(0.09)

os.system("clear")

os.system('figlet -f small "GHS JULIAN"|lolcat\n')


user_pass = input(color.BOLD+color.YELLOW+color.BOLD+"\n   [+] Enter Your Password :  "+color.LIGHT_CYAN)

used_password = []

algorithm = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', ]
guess = ""

while (guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = algorithm [randint(0, 25)]
        guess = str(guess_letter) + str(guess)
        used_password.append(guess)
        print(rnd.choice(color.color_list)+color.BOLD+"\n      Fetching Password "+color.RED+">>-->>  "+color.BOLD+color.YELLOW+guess)

os.system('clear && \n\nfiglet -f small "GHS JULIAN"|lolcat\n')
print (color.BOLD+'''       Congratulations Password Found !      \n'''+color.BOLD+color.YELLOW+'''
 +----------------------------------------------+'''+color.BOLD+color.BLUE+'''
 |                                              |
 |                                              |
'''+color.BOLD+color.RED+''' |         Your Password : '''+color.BOLD+color.LIGHT_GREEN+guess+'''              |
 |                                              |
'''+color.BOLD+color.GREEN+''' +----------------------------------------------+
''')
