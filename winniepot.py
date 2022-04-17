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

# get the host ip
def get_host(d):
  host = input(d.strftime("[+] [%Y-%m-%d %H:%M:%S] Target IP Host : "))
  return host

# get the ip port & check the range between 1 and 65535
def get_port(d):
  while True:
    try:
      port = int(input(d.strftime("[+] [%Y-%m-%d %H:%M:%S] Target port : ")))
    except TypeError:
      print("[-] Error => Invalid port number")
      continue
    else:
      if 1 < port > 65535:
        print("[-] Error => Invalid port number ")
        continue
      else:
        return port
        
# write the log to 
def write_log(client, data=''):
  border = "="*50
  f = open("./winniepot.mmh", "r+b")
  f.write("Time: %s\nIP: %s\nPort: %d\nData: %s\n%s\n\n" % (time.ctime(), client[0], client[1], data, border))
  f.close()

# main function to start the instance, pass in the host ipaddress and port
def start(host, port, d):
  border = "="*50
  print(d.strftime("[+] [%Y-%m-%d %H:%M:%S] Winniepot listening ..."))
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((host, port))
  s.listen(100)
  while True:
    insock, address = s.accept()
    print(d.strftime("[+] [%Y-%m-%d %H:%M:%S]  Connection Detected"))
    print("HIT from: %s:%d" % (address[0], address[1]))
    try:
      insock.send("%s\n"%(d))
      data = insock.recv(1024)
      insock.close()
    except socket.error as e:
      write_log(address)
    else:
      write_log(address, data)

# remember that datetime d in instantiated here 
if __name__ == "__main__":
  d = datetime.datetime.now()
  try:
    host = get_host(d)
    port = get_port(d)
    start(host, port, d)
  except KeyboardInterrupt:
    print("[-] Winniepot has been deactivated")
    exit(0)
  except Exception as e:
    print("Error : %s" % e)
    exit(1)

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



