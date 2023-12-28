import sys

def parse(code):
    lines=code.split("\n")
    keys=[]
    for i, line in enumerate(lines):
        if ";" in line:
            lines[i]=line[:line.find(";")]
        if len(lines[i]) > 0:
            keys.append(lines[i].split())
    return keys

def interpret(keys):
    for i in range(len(keys)):
        match k[0]:
            case "add":
                pass
            case "sub":
                pass
            case "out":
                pass
            case "in":
                pass
            case "ext":
                pass
            case "jif":
                pass
            case "sfig":
                pass
            case "sadr":
                pass

    return



if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Invalid amount of arguments!")
        sys.exit(1)
    interpret(parse(open(sys.argv[1], "r").read()))
