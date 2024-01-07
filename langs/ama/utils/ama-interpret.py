import sys

def error(msg):
  print(msg)
  sys.exit(1)

def clean(program):
  return [instruction for instruction in [line.split(';')[0].split() for line in program.split('\n')] if instruction != []]

def getOpcode(instruction):
  res = {
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
  'ext': 0xf}.get(instruction, 'NaN')
  if res == 'NaN':
    error('Instruction not found: ' + instruction)
  return res

def expand(keywords):
  expanded=[]
  for key in keywords:
    expanded_key=[]
    expanded_key.append(key[0])
    for i in range(len(key)-1):
      if key[i + 1][0] == '%':
        expanded.append(['set', ':' + hex(256 - len(key) + i)[2:], '!' + hex(int(key[i + 1].split('%')[1]))[2:]])
        expanded_key.append(':' + hex(256 - len(key) + i)[2:])
      else:
        expanded_key.append(key[i + 1])
    expanded.append(expanded_key)
  return expanded

def toCode(key, i):
  if i == 0:
    return getOpcode(key)
  if i != 0:
    return int(key[1:], 16)

def encode(keywords):
  encoded = [[toCode(key, i) for i, key in enumerate(instruction)] for instruction in keywords]
  return encoded

def format(program):
  return encode(expand(clean(program)))

def interpret(formatted):
  pass

if __name__ == '__main__':
  if len(sys.argv) != 2:
    error("Invalid number of arguments!")
  print(format(open(sys.argv[1], "r").read()))