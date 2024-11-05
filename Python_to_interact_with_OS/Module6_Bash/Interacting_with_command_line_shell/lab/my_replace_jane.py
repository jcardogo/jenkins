#!/usr/bin/env python3
import sys
import subprocess
import re

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    for line in lines:
        string=line.strip()
        #print(string)
        old_name = re.compile(r"jane", re.IGNORECASE)
        updated_strign= old_name.sub("jdoe", string)
        #print(updated_strign)
        cmd = ["mv", string, updated_strign]
        try:
            subprocess.run(cmd, check=True)
            print("File Renamed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
f.close()