import sys
def interpret(code):
    lines=code.split("\n")
    for i, line in enumerate(lines):
        lines[i]=line[:line.find(";")]
    for l in lines:
        print(l)

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Invalid amount of arguments!")
        sys.exit(1)
    interpret(open(sys.argv[1], "r").read())