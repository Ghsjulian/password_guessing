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
_load(color.YELLOW+"\n\n   [-] "+color.BROWN+color.BOLD+"Please Wait...\n")
_load(color.YELLOW+"\n\n   [-] "+color.GREEN+color.BOLD+"System Intilizing...\n\n")

os.system("clear || cls")
os.system('figlet -f small "GHS JULIAN"|lolcat\n\n')

print (color.BOLD+color.YELLOW+'''
 +----------------------------------------------+'''+color.BOLD+color.BLUE+'''
 |                                              |
 |                                              |
'''+color.BOLD+color.OKGREEN+''' |         SELECT  MENU           '''+color.BOLD+color.LIGHT_GREEN+'''              |
'''+color.BOLD+color.YELLOW+''' |   Random Password Checke ---[1]'''+color.BOLD+color.LIGHT_GREEN+'''              |
'''+color.BOLD+color.YELLOW+''' |   Password From List ---[2]    '''+color.BOLD+color.LIGHT_GREEN+'''              |
 |                                              |
'''+color.BOLD+color.GREEN+''' +----------------------------------------------+
''')
user_input = int(input(color.LIGHT_GREEN))

if user_input == 1:
  # TODO: write code...
  os.system("python random_password_cheaker.py")
elif user_input == 2:
  os.system("python list_password_cheaker.py")
else:
  print(color.BOLD+color.RED+"\n        Wrong Input Given     ")
  time.sleep(0.3)
  os.system("bash install.sh")