#imports-----------
from termcolor import colored, cprint
import threading
import keyboard
import time
import sys

#sprint------------
waiting_time = 0.01
def sprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(waiting_time)

#virgin------------
virginity = input("Is this your first time? (y/n)")

virgin = ["Yes", "yes", "Y", "y"]

if virginity in virgin:

  #intro-----------
  sprint("The year is 2038.")
  time.sleep(0.5)
  sprint("\n|\nThe US has invaded its surrounding countries and is looking to manifest more destiny.")
  time.sleep(0.5)
  sprint("\n|\nyou are in charge of a small country named\n")
  playerCountry = input("|\n")
  sprint("|\nThe world is at Defcon 1 and quickly devolving into madness\n")
  time.sleep(0.5)
  sprint("|\nYour objective is to develop your country and build as many Nukes as possible.\n\n")

else:
  sprint("What country do you control?\n")
  playerCountry = input()

#clicking----------
class colors:
  upaline = '\033[F'
  reset = '\033[0m'
  class fg:
    red = '\033[31m'
    orange = '\033[33m'
    yellow = '\033[93m'

time.sleep(0.5)
print(colors.fg.yellow,"     _.-^^---....,,--")
time.sleep(0.1)
print(colors.fg.yellow," _--                  --_")
time.sleep(0.1)
print(colors.fg.yellow,"<                        >)")
time.sleep(0.1)
print(colors.fg.orange,"|                         | ")
time.sleep(0.1)
print(colors.fg.orange," \._                   _./ ")
time.sleep(0.1)
print(colors.fg.orange,"    ```--. . , ; .--'''  ")
time.sleep(0.1)
print(colors.fg.red,"          | |   |")
time.sleep(0.1)
print(colors.fg.red,"       .-=||  | |=-.")
time.sleep(0.1)
print(colors.fg.red,"       `-=#$%&%$#=-")
time.sleep(0.1)
print(colors.fg.red,"          | ;  :|")
time.sleep(0.1)
print(colors.fg.red," _____.,-#%&$@%#&#~,._____")
time.sleep(0.5)

for i in range(3):
  print(colors.reset, ".")

print(playerCountry)

print("___________")
print("|  ENTER  |")
print("‾‾‾‾‾‾‾‾‾‾‾")

#vvv want free money?
money = 0
click = 1

times1 = 0

def clicked(m, c):
    m += 1
    c += 1
    return m, c

def spaced():
  global money
  while True:
    if times1 >= 1:
      print("$", money, end="\r")
      time.sleep(1/times1)
      money + 1
      continue

    else:
      continue

while True:
  if keyboard.is_pressed("enter"):
    money, click = clicked(money, click)
    print("$", money, end="\r")
    time.sleep(0.1)
    continue


  if money >= 50:
    print("\n___________")
    print("|    1    |")
    print("‾‾‾‾‾‾‾‾‾‾‾")
    print("\nHire Counterfeiter - $50 (1 mps)","\033[F\033[F\033[F\033[F\033[F\033[F")
    mk1 = threading.Thread(target=spaced)
    mk1.start()

    while True:
      if keyboard.is_pressed("1"):
        if money < 50:
          print("\n\n\n\n\nNot Enough Money!                 ")
          print("\033[FHire Counterfeiter - $50 (1 mps)\033[F\033[F\033[F\033[F\033[F\033[F")
          continue
        elif money >= 50:
          money -= 50
          print("$", money, end="\r")
          times1 += 1
          time.sleep(1)
          continue
  
      if keyboard.is_pressed("enter"):
        money, click = clicked(money, click)
        print("$", money, end="\r")
        time.sleep(0.1)
        continue

      if keyboard.is_pressed("!"):
        if money >= 50:
          for i in range(money/50):
            money -= 50
            print("$", money, end="\r")
            times1 += 1
            time.sleep(1)
            continue

        elif money < 50:
          print("\n\n\n\n\nNot Enough Money!                 ")
          time.sleep(1)
          print("\033[FHire Counterfeiter - $50 (1 mps)\033[F\033[F\033[F\033[F\033[F\033[F")
          continue