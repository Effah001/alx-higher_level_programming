#!/usr/bin/python3
import sys

def safe_function(fct, *args):
  try:
      result = fct(*args)
  except Exception as exp:
        print("Exception: {}".format(exp), file=stderr)
        return None
  finally:
        return result
