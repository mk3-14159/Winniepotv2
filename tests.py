#!/usr/bin/env python3
import socket
import sys
import selectors
import types

# Testing out the write log functionality
def write_log(phrase):
  with open("winniepot.log","a") as file_object:
    file_object.write(phrase)

# Single connection client test
def echo_server():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
      print(f"Connected by {addr}")
      while True:
        data = conn.recv(1024)
        if not data:
          break
        conn.sendall(data)

# Echo multi connection server
def service_connector(host, port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'testing ...')
    print(str(s.recv(4096), 'utf-8'))


if __name__ == "__main__":
  service_connector("192.168.1.13",9001)
