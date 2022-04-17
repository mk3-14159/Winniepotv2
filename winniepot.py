#!/usr/bin/env python3 
"""
https://github.com/mk3-14159/Winniepotv2 
Copyright (c) 2020 NUIG Honeypot FYP 
All rights reserved.
"""
import time
import socket
import datetime
import argparse
import os
import glob

# custom library imports
import animations


# prints banner logo located in the ../../banner directory
def import_banner():
  with open("banner/banner.txt", "r") as f:
    for line in f:
      print(line.rstrip())

# Datetime prompt 
def get_input():
  d = datetime.datetime.now()
  print("datetime : %s" % d)

if __name__ == "__main__":
  animations.animation_bar_load()
  



"""
  parser = argparse.ArgumentParser(
  description='Honeypot demonstration project'
  )
  parser.add_argument(
  '-ip',
  '--ip',
  action = 'store',
  dest = 'ip_address',
  help='input local ip address to set up the honeypot'
  )
  args = parser.parse_args()
  ip_address = args.ip_address
  main()
"""



