# ⚠️SPECIFICATION NOT YET COMPLETE⚠️
# Specification for AMA v1.4  
## Contents of this specification  
## General Information  
The "advanced minimalistic assembly", in short AMA, operates on 32 bit registers  
and 8 bit memory cells (see [DATA STORAGE](#data-storage)). This language will in most cases be  
compiled to an intermediate byte code in the form of an .XPF ("executable program  
file") file (see [INSTRUCTION ENCODING SPECIFICATION](#instruction-encoding-specification), [CORRUPTION DETECTION](#corruption-detection))  
or be interpreted directly as an .AMA file. The intermediate byte code will  
then be interpreted by a runtime environment.  
## Data Storage  
### Registers  
This language uses 8 general purpose 32 bit registers with register 0 being used as the program  
counter holding the index of the current instruction (see [SPECIFICATIONS FOR COMPILERS AND INTERPRETERS](#specifications-for-compilers-and-interpreters)).  
These values are initialized as 0.  
### Memory  
This language uses a memory with 32 bit addresses. Each memory cell contains  
8 bits. All values are initialized as 0.  
### Flag  
The flag is a boolean value, which can be modified by the [FLAG OPERATIONS](#flag-operations).  
Initialized as false.  
### Stack  
The stack is a stack of 32 bit values, which can be used with the  
[STACK OPERATIONS](#stack-operations). Initialized as empty.  
### I/O streams
The I/O streams are queues used for input/output handling (see [I/O STREAM SPECIFICATIONS](#io-stream-specifications).  
These can be used with the [I/O STREAM INSTRUCTIONS](#io-stream-instructions).  
## Instruction set specification  
### Stack operations  
|Instruction with arguments|Function|
|-|-|
|PUSH $r1|Push value in register r1 onto stack.|
|POP $r1|Pop value of stack into register r1.|
### Arithmetic/Logic  
|Instruction with arguments|Function|
|-|-|
|ALI $OP $r1 $r2 $r3|Applies the $OP [ARITHMETIC/LOGIC INSTRUCTION](#arithmeticlogic-instruction) to r1 and r2. Result is put into r3.|
### I/O stream instructions
|Instruction with arguments|Function|
|-|-|
|HIOS $STREAM $r1|Depending on, if STREAM is an input or an output stream, either push value in r1 into STREAM or pop value of STREAM into r1.|
|POS $STREAM|Proccess output STREAM by emptying it and outputting it.|
### Memory instructions  
|Instruction with arguments|Function|
|-|-|
|LOD $r1 $r2|Load register r1 with the value combining the 4 memory cells beginning at the adress given by the value in r2.|
|STO $r1 $r2|Store into the 4 memory cells beginning at the address given by the value in r2 with the value in r1.|
|STI $r1 #val|Set the 4 memory cells beginning at the address given by the value in r1 to val.|
### Register instructions
|Instruction with arguments|Function|
|-|-|
|LDI $r1 !val|Load val into r1.|
|MOV $r1 $r2|Load value in r1 into r2.|
|CMOV $r1 $r2|Load value in r1 into r2 only if the flag is true.|
### Flag operations  
|Instruction with arguments|Function|
|-|-|
|NF|Negates flag.|
|SFL $r1 $r2|Sets flag to true, if value in r1 is less than the value in r2, else sets flag to false.|
|SFG $r1 $r2|Sets flag to true, if value in r1 is greater than the value in r2, else sets flag to false.|
|SFE $r1 $r2|Sets flag to true, if value in r1 is equal to the value in r2, else sets flag to false.|
### Extended  
|Instruction with arguments|Function|
|-|-|
|UXIS #OPC $r1|Executes extended instruction with the opcode given by OPC with the value in r1 as the argument.|
## Instruction encoding specification  
|Opcode in hexadecimal|Instruction with arguments|Bit usage|Encoded Size|
|-|-|-|-|

For more information on instructions see [INSTRUCTION SET SPECIFICATION](#instruction-set-specification).  
To understand how redundant bits are used see [CORRUPTION DETECTION](#corruption-detection).  
## Corruption detection  
  
## Specifications for compilers and interpreters  
When building a compiler or an interpreter for AMA it should obey the following:  
-In case your compiler or interpreter uses [TEMPORARY REGISTERS](#temporary-registers) it should  
   output an warning and stop when register 253, 254 or 255 is being  
   edited (for reason see [TEMPORARY REGISTERS](#temporary-registers)).  
-When detecting a ; it should ignore the ; and the rest of the line, because  
   a ; represents the start of a comment.
-For compilers and runtime environments the specified [CORRUPTION DETECTION](#corruption-detection)  
   should be implemented.  
-Have the specified [FILE-EXTERNAL INSTRUCTUIONS](#specification-of-file-external-instructions) implemented. Also applys  
   for runtime environments.  
-Take all numbers as hexadecimal.  
-Implement the [DATA STORAGE](#data-storage) as specified.  
## Specification of extended instructions  
Here the [EXTENDED INSTRUCTIONS](#extended) are specified:  
|Opcode|Instruction|Function|
|-|-|-|
|0|EXIT|Exits program with exit code given by the argument.|
|1|NOP|Does nothing.|
|2|WAIT|Waits an amount of milliseconds given by the argument.|
|3|GETM|Allocates the argument * 4 bytes in RAM.|

Any opcode larger should be ignored.  
