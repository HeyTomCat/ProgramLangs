# Specification for AMA v1.0  
## Contents of this specification  
-[Contents of this specification](#contents-of-this-specification)  
-[General Information](#general-information)  
-[Data Storage](#data-storage)  
   -[Registers](#registers)  
   -[Memory](#memory)  
   -[Flag](#flag)  
   -[Stack](#stack)  
-[Instruction set specification](#instruction-set-specification)  
   -[Stack operations](#stack-operations)  
   -[Arithmetic](#arithmetic)  
   -[Register instructions](#register-instructions)  
   -[Flag operations](#flag-operations)  
   -[Branching](#branching)  
   -[External](#external)  
-[Instruction encoding specification](#instruction-encoding-specification)  
-[Corruption detection](#corruption-detection)  
-[Specifications for compilers and interpreters](#specifications-for-compilers-and-interpreters)  
-[Specification of file-external instructions](#specification-of-file-external-instructions)
-[Temporary registers](#temporary-registers)
## General Information  
The "advanced minimalistic assembly", in short AMA, operates on 32 bit registers  
and 8 bit memory cells (see [DATA STORAGE](#data-storage)). This language will in most cases be  
compiled to an intermediate byte code in the form of an .EEA ("executable encoded  
assembly") file (see [INSTRUCTION ENCODING SPECIFICATION](#instruction-encoding-specification), [CORRUPTION DETECTION](#corruption-detection))  
or be interpreted directly as an .AMA file. The intermediate byte code will  
then be interpreted by a runtime environment.  
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
|lm :radr :r|Load the 4 memory cells ending at the address given by the value in radr with the value in r.|
|mov :r1 :r2|In pseudocode: r2 = r1|
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
|ext :rop :rarg|Executes the file-external instruction with the opcode given by the value in memory with the address given by the value in rop, argument register given by the value in rarg (see [SPECIFICATION OF FILE-EXTERNAL INSTRUCTIONS](#specification-of-file-external-instructions)).|
## Instruction encoding specification  
|Opcode in hexadecimal|Instruction with arguments|Bit usage|Encoded Size|
|-|-|-|-|
|0|push :r|4b redundant, 4b opcode, 8b r|2B|
|1|pop :r|4b redundant, 4b opcode,  8b r|2B|
|2|add :r1 :r2 :r3|4b redundant, 4b opcode, 8b r1, 8b r2, 8b r3|4B|
|3|sub :r1 :r2 :r3|4b redundant, 4b opcode, 8b r1, 8b r2, 8b r3|4B|
|4|mult :r1 :r2 :r3|4b redundant, 4b opcode, 8b r1, 8b r2, 8b r3|4B|
|5|lr :r :radr|4b redundant, 4b opcode, 8b r, 8b radr|3B|
|6|lm :radr :r|4b redundant, 4b opcode, 8b r, 8b radr|3B|
|7|mov :r1 :r2|4b redundant, 4b opcode, 8b r1, 8b r2|3B|
|8|set :r !val|4b redundant, 4b opcode, 8b r, 32b val|6B|
|9|nf|4b redundant, 4b opcode|1B|
|a|sfl :r1 :r2|4b redundant, 4b opcode, 8b r1, 8b r2|3B|
|b|sfg :r1 :r2|4b redundant, 4b opcode, 8b r1, 8b r2|3B|
|c|sfe :r1 :r2|4b redundant, 4b opcode, 8b r1, 8b r2|3B|
|d|jmp :r|4b redundant, 4b opcode, 8b r|2B|
|e|jpc :r|4b redundant, 4b opcode, 8b r|2B|
|f|ext :rop :rarg|4b redundant, 4b opcode, 8b rop, 8b rarg|3B|  

For more information on instructions see [INSTRUCTION SET SPECIFICATION](#instruction-set-specification).  
To understand how redundant bits are used see [CORRUPTION DETECTION](#corruption-detection).  
## Corruption detection  
When encoded, there are 4 redundant bits per instruction that are used  
for corruption detection. Those bits are usually all set to 0 and if  
the runtime environment finds, that at least 1 of those bits isn't 0  
it knows there was a corruption and should output an error.  
## Specifications for compilers and interpreters  
When building a compiler or an interpreter for AMA it should obey the following:  
-Output an error and stop when register 0 is being edited (for reason see  
   [REGISTERS](#registers)). This should also be the case for runtime environments.  
-In case your compiler or interpreter uses [TEMPORARY REGISTERS](#temporary-registers) it should  
   also output an error and stop when register 253, 254 or 255 is being  
   edited (for reason see [TEMPORARY REGISTERS](#temporary-registers)).  
   This DOES NOT apply to runtime environments.  
-When detecting a ; it should ignore the ; and the rest of the line, because  
   a ; represents the start of a comment.
-For compilers and runtime environments the specified [CORRUPTION DETECTION](#corruption-detection)  
   should be implemented.  
-Have the specified [FILE-EXTERNAL INSTRUCTUIONS](#specification-of-file-external-instructions) implemented. Also applys  
   for runtime environments.  
-Take all numbers as hexadecimal.
## Specification of file-external instructions  
Here the [FILE-EXTERNAL COMMANDS](#external) are specified:  
|Opcode|Instruction|Function|
|-|-|-|
|0|halt|Exits program with exit code given by the value in the argument register.|
|1|noop|Does nothing.|
|2|sleep|Waits an amount of milliseconds given by the value in the argument register.|
|3|out|Outputs all registers from argument register to next 0-valued register as UTF-32.|
|4|in|Takes UTF-32 input into registers from argument register to next 0-valued register. Further input ignored.|

Any opcode larger should be ignored.  
## Temporary registers  
This is an optional feature for AMA compilers and interpreters which makes  
coding easier and makes the code look cleaner. With this you can, instead of a  
register as :r with r being the register number, write an integer as [n] with  
n being the integer. It should be implemented by writing before the instruction  
a set instruction, setting one of the "temporary registers" (usually register 253,  
254 or 255) to the integer. This has the same effect as using that number  
directly, just it doesn't need to change the instructions.  
