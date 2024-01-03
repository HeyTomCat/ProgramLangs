# !SPECIFICATION NOT YET COMPLETE!  
# Specification for AMA  
## Contents of this specification  
-[General Information](#general-information)  
-[Data Storage](#data-storage)  
   -[Registers](#registers)  
   -[Memory](#memory)  
-[Instruction set specification](#instruction-set-specification)  
-[Instruction encoding specification](#instruction-encoding-specification)  
-[Corruption detection](#corruption-detection)  
-[Specifications for compilers and interpreters](#specifications-for-compilers-and-interpreters)  
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
### Memory  
This language uses a memory with 32 bit adresses. Each memory cell contains  
8 bits.  
### Flag  
The flag is a boolean value, which can be set by the [FLAG OPERATIONS](#flag-operations).  
### Stack  
## Instruction set specification  
### Stack operations  
### Arithmetic  
### Register instructions  
### Flag operations  
### Branching  
### External
## Instruction encoding specification  
## Corruption detection  
## Specifications for compilers and interpreters  
