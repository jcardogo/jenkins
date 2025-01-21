#!/usr/bin/env python3

"""
#Basic try/except code 
try:
  print(x)
except NameError:
  print("Variable x is not defined")
"""

"""
#More advanced try/except code adding extra error
try:
  f = open("etc/hosts", "w+")
  f.write("success!")
except FileNotFoundError:
  print("Data file not found")
except Exception as ex:
  print("Error appending to file: " + str(ex))
else:
  f.close()
"""

"""
x = "hello"
if not isinstance(x, int):
  raise TypeError("Only integers are allowed")
"""
def start_server(port):
  if not isinstance(port, int):
    raise TypeError("Port number must be an integer")
  elif port < 1024 or port > 65535:
    raise ValueError ("Port number is invalid")
x = input("Enter port number: ")
try:
  port = int(x)
  print("You entered: ", port)
  print(type(port))
except ValueError:
  print("Invalid input. please enter a valid integer.")

start_server(port)
