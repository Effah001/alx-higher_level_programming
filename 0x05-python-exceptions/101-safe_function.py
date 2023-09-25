#!/usr/bin/python3
import sys

def safe_function(fct, *args):
  try:
      result = fct(*args)
    except Exception as exp:
        print(f"Exception: {exp}", file=sys.stderr)
        return None
    finally:
        return result
