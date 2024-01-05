import sys

def parse(program):
  #removes comments and splits up into keywords
  return [instruction for instruction in [line.split(';')[0].split() for line in program.split('\n')] if instruction != []]

opcode = {
  'push': 0x0,
  'pop': 0x1,
  'add': 0x2,
  'sub': 0x3,
  'mult': 0x4,
  'lr': 0x5,
  'lm': 0x6,
  'mov': 0x7,
  'set': 0x8,
  'cmov': 0x9,
  'setm': 0xa,
  'nf': 0xb,
  'sfl': 0xc,
  'sfg': 0xd,
  'sfe': 0xe,
  'ext': 0xf
}

exspected_args = [
  (1, [':']),
  (1, [':']),
  (),
  (),
  (),
  (),
  (),
  (),
  (),
  (),
  (),
  (),
  (),
  (),
  (),
  ()
]

def decode(instruction):
  pass

def interpret(keywords):
  pass

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Invalid number of arguments!")
    sys.exit(1)
  interpret(parse(open(sys.argv[1], "r").read()))
