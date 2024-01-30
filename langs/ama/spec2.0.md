# ⚠️Specification not yet complete⚠️
# Specification for AMA v2.0
## Contents of this specification
## General Information
The "advanced minimalistic assembly", or short AMA, is a programming language with an assembly-like syntax. Saved in .AMA files, programs should usually be "assembled" to an .XAP (eXecutable Assembled Program) file and then be executed by a runtime environment. The language is designed to be light-weight and to have a minimalistic instruction set.  
## Data Storage
### Registers
This language operates on 8 registers, called R0, R1, R2, R3, R4, R5, R6 and R7, of 32 bits each, all initialized as 0. The register R0 holds the index of the currently being executed instruction and when written to leads to instruction jumps.  
### Memory
This language uses a memory with 32 bit addresses, therefore 4294967296 memory cells, each containing 8 bit. All cells are initialized as 0. Memory can't be used unless allocated.  
### Flag
The flag is a 1 bit boolean value initialized as false.  
### Stack
The stack is a stack of 32 bit values initialized as empty.  
### I/O Streams
The I/O Streams are 8 different queues of 32 bit values.  
|ID|NAME|FUNCTION|
|-|-|-|
|0|NULL|Discards when used as output, returns 0 when used as input|
|1|SYST|Interaction with system|
|2|META|Data stream containing the meta-data string. Equivalent to DAT0.|
|2|DAT0|Data stream containing the meta-data string. Equivalent to META.|
|3|DAT1|General purpose data stream|
|4|DAT2|General purpose data stream|
|5|DAT3|General purpose data stream|
|6|DAT4|General purpose data stream|
|7|DAT5|General purpose data stream|
## Execution cycle
AMA executes all instructions using a special execution cycle:  
**1.** Load instruction from instruction memory with program counter (R0).  
**[OPTIONAL]** Translate instruction to micro-instructions.  
**2.** Execute instruction.  
**3.** Check for change in program counter to execute instruction jumps *immediatly*.  
**4.** Increment program counter.  
**5.** Repeat.  
## Instructions
Here all 32 instructions, their opcodes and their function are listed.  
|OPCODE|INSTRUCTION|FUNCTION|
|-|-|-|
|0|||
|1|||
|2|||
|3|||
|4|||
|5|||
|6|||
|7|||
|8|||
|9|||
|10|||
|11|||
|12|||
|13|||
|14|||
|15|||
|16|||
|17|||
|18|||
|19|||
|20|||
|21|||
|22|||
|23|||
|24|||
|25|||
|26|||
|27|||
|28|||
|29|||
|30|||
|31|||
