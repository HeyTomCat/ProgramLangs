import sys

def parse(program):
  return [line.split(';')[0].split() for line in program.split('\n')]

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Invalid number of arguments!")
    sys.exit(1)
  print(parse(open(sys.argv[1], "r").read()))
