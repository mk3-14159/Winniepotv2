#!/usr/bin/env python3 
"""
https://github.com/mk3-14159/Winniepotv2
Copyright (c) 2020 NUIG Honeypot FYP
All rights reserved.
"""
import time
import sys
import threading
import itertools
from termcolor import colored
from tqdm import tqdm

# animation = ["10%", "20%", "30%" ... "100%"]
def animation_bar_load():
  print(colored(" [+] Loading Winniepot :", "red"))
  animation = ["10% ■□□□□□□□□□]"
              ,"20% ■■□□□□□□□□]"
              ,"30% ■■■□□□□□□□]"
              ,"40% ■■■■□□□□□□]"
              ,"50% ■■■■■□□□□□]"
              ,"60% ■■■■■■□□□□]"
              ,"70% ■■■■■■■□□□]"
              ,"80% ■■■■■■■■□□]"
              ,"90% ■■■■■■■■■□]"
              ,"100% ■■■■■■■■■■]"]
  for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

# success animation
def animation_success():
  print("Deploying Winniepot : ")
  print('\x1b[6;30;42m' + 'Success! \n' + '\x1b[0m')

# itertools arrow animation - don't use this  
def animation_arrow_load():
    done = False
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')
    t = threading.Thread(target=animate)
    t.start()
    time.sleep(5)
    done = True

# trying animation from tqdm library
def animation_tqdm():
  for i in tqdm(range(100)):
    time.sleep(0.01)

"""
if __name__ == "__main__":
  animation_tqdm()
  animation_success()
"""
