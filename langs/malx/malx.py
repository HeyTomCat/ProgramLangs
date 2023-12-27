import sys
def interpret(code):
    lines=code.split("\n")
    keys=[]
    for i, line in enumerate(lines):
        if ";" in line:
            lines[i]=line[:line.find(";")]
        if len(lines[i]) > 0:
            keys.append(lines[i].split())
    for k in keys:
        print(k)
        print("TEST")

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Invalid amount of arguments!")
        sys.exit(1)
    interpret(open(sys.argv[1], "r").read())
