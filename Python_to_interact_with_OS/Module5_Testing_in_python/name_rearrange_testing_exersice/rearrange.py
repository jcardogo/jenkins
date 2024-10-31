#!/usr/bin/env python3

import re

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  if result is None: #we incuided this check to avoid edge error on unittest over empty string as input ton the function
    return name
  return "{} {}".format(result[2], result[1])


