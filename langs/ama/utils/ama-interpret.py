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

def none():
  pass

stack = []
register = [0 for i in range(256)]
flag = False

def setRegister(r, val):
  register[r] = val
  return r == 0

def setRegisterC(r, val, flag):
  if flag:
    setRegister(r, val)
    return r == 0

def setFlag(new):
  flag = new

cmds = [
(lambda args: stack.append(register[args[0]])),
(lambda args: setRegister(args[0], stack.pop())),
(lambda args: setRegister(args[2], register[args[0]] + register[args[1]])),
(lambda args: setRegister(args[2], register[args[0]] - register[args[1]])),
(lambda args: setRegister(args[2], register[args[0]] * register[args[1]])),
(lambda args: error('LR not yet implemented!')),
(lambda args: error('LM not yet implemented!')),
(lambda args: setRegister(args[1], register[args[0]])),
(lambda args: setRegister(args[0], args[1])),
(lambda args: setRegisterC(args[1], register[args[0]], flag)),
(lambda args: error('SETM not yet implemented!')),
(lambda args: setFlag(not flag)),
(lambda args: setFlag(register[args[0]] < register[args[1]])),
(lambda args: setFlag(register[args[0]] > register[args[1]])),
(lambda args: setFlag(register[args[0]] == register[args[1]])),
(lambda args: error('EXT not yet implemented!'))
]

def interpret(formatted):
  while register[0] < len(formatted):
    pcSet=False
    op = formatted[register[0]][0]
    args = formatted[register[0]][1:]
    cmds[op](args)
    if not pcSet:
      register[0] += 1

if __name__ == '__main__':
  if len(sys.argv) != 2:
    error("Invalid number of arguments!")
  interpret(format(open(sys.argv[1], "r").read()))