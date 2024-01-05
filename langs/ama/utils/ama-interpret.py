import sys
if __name__=='__main__':
  if len(sys.argv) != 2:
    print("Invalid number of arguments!")
  open(sys.argv[1], "r").read()
