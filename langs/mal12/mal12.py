import sys
tokens=open(sys.argv[1]).read().split()
compiled_length=0
cmdis=[]
i=0
while i<len(tokens):
    token=tokens[i]
    if not (token[0]=='#' or token[0]=='$' or token[0]=='*'):
        cmdis.append(i)
    i+=1
