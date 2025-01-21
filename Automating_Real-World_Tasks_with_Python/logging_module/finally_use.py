#!/usr/bin/env python3

try: 
  f = open("/etc/hosts", "w+")
except:
  print("Error appending to file: " + str(ex))
finally:
  f.close() #causes error if the file could not be opened
