# ⚠️Specification not yet complete⚠️
# Specification for AMA v2.0
## Contents of this specification
## General Information
The "advanced minimalistic assembly", or short AMA, is a programming language with an assembly-like syntax. Saved in .AMA files, programs should usually be "assembled" to an .XAP (eXecutable Assembled Program) file and then be executed by a runtime environment. The language is designed to be light-weight and to have a minimalistic instruction set.  
## Data Storage
### Registers
This language operates on 8 registers, called r0, r1, r2, r3, r4, r5, r6 and r7, of 32 bits each, all initialized as 0. The register R0 holds the index of the currently being executed instruction and when written to leads to instruction jumps.  
### Memory
This language uses a memory with 32 bit addresses, therefore 4294967296 memory cells, each containing 8 bit. All cells are initialized as 0. Memory can't be used unless allocated.  
### Flag
The flag is a 1 bit boolean value initialized as false. Can be set (True) and reset (False).  
### Stack
The stack is a stack of 32 bit values initialized as empty.  
### I/O Streams
The I/O Streams are 8 different queues of 32 bit values.  
|ID|NAME|FUNCTION|
|-|-|-|
|0|null|Discards when used as output, returns 0 when used as input|
|1|syst|Interaction with system|
|2|meta|Data stream containing the meta-data string. Equivalent to dat0.|
|2|dat0|Data stream containing the meta-data string. Equivalent to meta.|
|3|dat1|General purpose data stream|
|4|dat2|General purpose data stream|
|5|dat3|General purpose data stream|
|6|dat4|General purpose data stream|
|7|dat5|General purpose data stream|
## Execution cycle
AMA executes all instructions using a special execution cycle:  
**1.** Load instruction from instruction memory with program counter (R0).  
**[OPTIONAL]** Translate instruction to micro-instructions.  
**2.** Execute instruction.  
**3.** Check for change in program counter to execute instruction jumps *immediatly*.  
**4.** Increment program counter.  
**5.** Repeat.  
## Instructions
Here all 32 instructions, their opcodes in hexadecimal and their function are listed. Registers are written as rN with N being a hexadecimal number, 3 bit integers as #N, 8 bit integers as $N and 32 bit integers as !N.  
|OPCODE IN HEX|INSTRUCTION|FUNCTION|
|-|-|-|
|00|nop|Does nothing.|
|01|push r1|Pushes value in r1 onto stack.|
|02|pop r1|Pops value of the stack into r1.|
|03|ali #op r1 r2 r3|Applys #op arithmetic/logic instruction to r1 and r2. Result is put into r3.|
|04|i #stream r1|Pops from i/o #stream into r1.|
|05|o #stream r1|Pushes onto i/o #stream from r1.|
|06|ld-ir !i r1|Loads !i into r1.|
|07|ld-im $i r1|Loads $i into the memory cell with the address given by the value in r1.|
|08|ld-rr r1 r2|Copys value in r1 into r2.|
|09|ld-rm r1 r2|Copys value in r1 into the 4 memory cells beginning at the address given by the value in r2.|
|0a|ld-ra r1 !a|Copys value in r1 into the 4 memory cells beginning at the address !a.|
|0b|ld-mr r1 r2|Copys value in the 4 memory cells beginning at the address given by the value in r1 into r2.|
|0c|cld-ir !i r1|Loads !i into r1 if the flag is set.|
|0d|cld-im $i r1|Loads $i into the memory cell with the address given by the value in r1 if flag is set.|
|0e|cld-rr r1 r2|Copys value in r1 into r2 if flag.|
|0f|cld-rm r1 r2|Copys value in r1 into the 4 memory cells beginning at the address given by the value in r2 if flag is set.||
|10|cld-mr r1 r2|Copys value in the 4 memory cells beginning at the address given by the value in r1 into r2 if flag is set.|
|11|nf|Negates flag. If flag is set resets flag and if flag is reset sets.|
|12|sfl r1 r2|Sets flag if r1 < r2. Else resets flag.|
|13|sfe r1 r2|Sets flag if r1 == r2. Else resets flag.|
|14|sf|Sets flag.|
|15|rf|Resets flag.|
|16|pushi !i|Pushes !i onto stack.|
|17|alii #op r1 !i r2|Applys #op arithmetic/logic instruction to r1 and !i. Result is put into r2.|
|18|subi !i r1 r2|Computes !i minus the value in r1. Result is put into r2.|
|19|oi #stream !i|Pushes !i onto i/o #stream.|
|1a|sfli r1 !i|Sets flag if r1 < !i. Else resets flag.|
|1b|sfei r1 !i|Sets flag if r1 == !i. Else resets flag.|
|1c|debug|Enter debug mode.|
|1d|alloc !start !end|Allocates memory from memory address !start to memory adress !end.|
|1e|sys #op $arg|Executes system instruction #op with argument #arg.|
|1f|exit #n|Exits with exit code #n.|
