#!/usr/bin/env python3 
"""
https://github.com/mk3-14159/Winniepotv2 
Copyright (c) 2020 NUIG Honeypot FYP 
All rights reserved.
"""
import time
import socket
import datetime
import os
import glob
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging 

# custom library imports
from animations import *

# HTTP handler class
class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("Winniepot Decoy Module (deceptive server environment) {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Winniepot is listening...\n')
    animation_success()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping Winniepot...\n')


# prints banner logo located in the ../../banner directory
def import_banner():
  with open("banner/banner.txt", "r") as f:
    for line in f:
      print(line.rstrip())


# Write the http log into a mmh file 
'''
def write_log(client, data=''):
  border = "="*50
  f = open("./winniepot.mmh", "a")
  f.write("Time: %s\nIP: %s\nPort: %d\nData: %s\n%s\n\n" % (time.ctime(), client[0], client[1], data, border))
  f.close()
'''

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
  from sys import argv
  import_banner()
  # animation_arrow_load()
  d = datetime.datetime.now()
  print("Winniepot instance started at %s" % d)
  animation_tqdm()

  border = "="*50
  f = open("winniepot.log", "a")

  # runtime
  if len(argv) == 2:
    run(port=int(argv[1]))
    # f.write(run(port=int(argv[1])))
  else:
    run()
    # f.write(run())




