# !SPECIFICATION NOT YET COMPLETE!  
# Specification for AMA  
## Contents of this specification  
-[Contents of this specification](#contents-of-this-specification)
-[General Information](#general-information)  
-[Data Storage](#data-storage)  
   -[Registers](#registers)  
   -[Memory](#memory)  
-[Instruction set specification](#instruction-set-specification)  
-[Instruction encoding specification](#instruction-encoding-specification)  
-[Corruption detection](#corruption-detection)  
-[Specifications for compilers and interpreters](#specifications-for-compilers-and-interpreters)  
-[Specification of file-external instructions](#specification-of-file-external-instructions)
## General Information  
The "advanced minimalistic assembly", in short AMA, operates on 32 bit registers  
and 8 bit memory cells (see [DATA STORAGE](#data-storage)). This language will in most cases be  
compiled to an intermediate byte code in the form of an .EEA ("executable encoded  
assembly") file (see [INSTRUCTION ENCODING SPECIFICATION](#instruction-encoding-specification), [CORRUPTION DETECTION](#corruption-detection))  
or be interpreted directly as an .AMA file. The intermediate byte code will  
then be interpreted by a compilation interpreter.  
## Data Storage  
### Registers  
This language uses 256 registers with register 0 being used as the program  
counter and being uneditable (see [SPECIFICATIONS FOR COMPILERS AND INTERPRETERS](#specifications-for-compilers-and-interpreters).  
Each of these registers contain 32 bits in the form of 32 bit unsigned integers.  
By standard are all values 0.  
### Memory  
This language uses a memory with 32 bit addresses. Each memory cell contains  
8 bits. By standard are all values 0.  
### Flag  
The flag is a boolean value, which can be set by the [FLAG OPERATIONS](#flag-operations).  
By standard false.  
### Stack  
The stack is a stack of 32 bit unsigned integers which can be changed by the  
[STACK OPERATIONS](#stack-operations). By standard empty.  
## Instruction set specification  
### Stack operations  
|Instruction with arguments|Function|
|-|-|
|push :r|Push value in register r onto stack.|
|pop :r|Pop value of stack into register r.|
### Arithmetic  
|Instruction with arguments|Function in pseudocode|
|-|-|
|add :r1 :r2 :r3|r3 = r1 + r2|
|sub :r1 :r2 :r3|r3 = r1 - r2|
|mult :r1 :r2 :r3|r3 = r1 * r2|
### Register instructions  
|Instruction with arguments|Function|
|-|-|
|lr :r :radr|Load the register r with the value in the 4 memory cells beginning with the address given by the value in radr.|
|lm :radr :r|Load the 4 memory cells beginning at the address given by the value in radr with the value in r.|
|mov :r1 :r2|In pseudocode: r1 = r2|
|set :r !val|With val an 32 bit unsigned integer, in pseudocode: r = val|
### Flag operations  
|Instruction with arguments|Function in pseudocode|
|-|-|
|nf|flag = not flag|
|sfl :r1 :r2|flag = r1 < r2|
|sfg :r1 :r2|flag = r1 > r2|
|sfe :r1 :r2|flag = r1 == r2|
### Branching  
|Instruction with arguments|Function|
|-|-|
|jmp :r|Jump to instruction given by the value in r.|
|jpc :r|Jump to instruction given by the value in r if flag is set to true.|
### External
|Instruction with arguments|Function|
|-|-|
|ext :rop :rarg||
## Instruction encoding specification  
## Corruption detection  
## Specifications for compilers and interpreters  
## Specification of file-external instructions
