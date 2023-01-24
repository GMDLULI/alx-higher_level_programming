#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value)
        return (True)
    except (TypeError, ValueError):
        print("Execptions:{}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
   
