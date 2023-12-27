import sys
def interpret(code):
    lines=code.split("\n")
    print(code)
if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Invalid amount of arguments!")
        sys.exit(1)
    interpret(open(sys.argv[1], "r").read())