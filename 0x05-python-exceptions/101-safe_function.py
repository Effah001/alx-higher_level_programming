#!/usr/bin/python3
import sys

def safe_function(fct, *args):
  try:
      err = fct(*args)
    except BaseException as exp:
        print(f"Exception: {exp}", file=sys.stderr)
        return None
    finally:
        return err
