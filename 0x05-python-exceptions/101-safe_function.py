#!/usr/bin/python3
import sys

def safe_function(fct, *args):
  try:
      err = fct(*args)
    except BaseException as exp:
        print("Exception: {}".format(exp), file=stderr)
        return None
    finally:
        return err
