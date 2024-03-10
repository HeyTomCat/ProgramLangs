# Specification for AMS 1.4 u1
## Contents of this specification
## Introduction
AMS, which is short for "advanced minimalistic assembly", is an 8-bit register-based programming language with an assembly-inspired syntax.  
It is compiled to a special bytecode before being executed by a runtime environment. Alternatively it can be compiled to native machine code or assembly.  
## Data storage
### Registers
AMS uses a total of 8 registers, each containing 8 bits of information, which are the only directly accessible type of data storage. Most of them have different purposes which are listed in the following table:  
|Register name|Register|Purpose|
|-|-|-|
|C|r0|Low byte of program counter|
|P|r1|High byte of program counter|
|L|r2|Low byte of address|
|H|r3|High byte of address|
|F|r4|Flags register|
|A|r5|General purpose register A|
|B|r6|General purpose register B|
|I|r7|Register for [IMPLICIT VALUE USAGE](#implicit-value-usage)|
  
***NOTICE:** The value in a register can't exceed the 8-bit unsigned integer limit.*

### RAM
AMS uses 64KB of RAM. In this RAM the working memory **and** the program memory is included.  
  
***NOTICE:** The working memory isn't the full 64 KB, since the program is included in the RAM too.*

### Disk
AMS has access to 4GB of disk space. It is divieded into 64K blocks of 64KB each. Some of these blocks have special purposes displayed in the table below.  

|Block (Hexadecimal)|Name|Purpose|
|-|-|-|
|0000|RAM|Reading from this block will result in the [RAM](#ram). Writing to it will write to the [RAM](#ram).|
|0001|NUL|Even though not enforced, this block should be kept free for the purpose of easy freeing of other blocks.|
|0002|TMP|This block should be mostly kept free for the purpose of saving important data from the disk access block, when other data is currently being read.|
|0003|CON|This block represents the contents of the console.|
|0004|SYS|Block reserved for system code|
|0005-FFFF|General purpose blocks|General purpose blocks that can be used as general disk space.|

***NOTICE:** The whole 4GB can't be used as disk space, since 5 * 64KB are required for other purposes.*

## Type syntax
The syntax for the different data types in AMS is listed in the table below.  

|Syntax|Type|
|-|-|
|`r[DIGIT]` / [See register names](#registers)|[Register](#registers)|
|`$[HEX DIGIT][HEX DIGIT]`|8-bit unsigned integer|
|`%[HEX DIGIT][HEX DIGIT]`|[IMPLICIT VALUE](#implicit-value-usage) (Optional)|
|`{SOMETHING}`|Explained in close proximity to usage|

## List of instructions
AMS uses a total of 16 instructions with different purposes. These are listed in the tables below.  

## Access context
The access context is 16 bit specifier for the [Memory / Disk instructions](#memory--disk-instructions) from where to read or where to write to. These map directly to the addresses of the [Disk blocks](#disk), including special blocks like [RAM](#disk).  

### NOP & HLT
|OP Code (hex)|Instruction|Example|Function in example|
|-|-|-|-|
|0|NOP|`nop`|Does nothing|
|1|HLT|`hlt $00`|Halts program with exit code `00`|

### Register instructions
|OP Code (hex)|Instruction|Example|Function in example|
|-|-|-|-|
|2|LDI|`ldi r0 $00`Loads value `00` into register `r0`|
|3|MOV|`mov r0 r1`|Copys value in r0 into r1|

### Memory / Disk instructions
|OP Code (hex)|Instruction|Example|Function in example|
|-|-|-|-|
|4|STR|`str r0`|Stores value in register `r0` into the [access context](#access-context) loction given by the [L and H registers](#registers)|
|5|LDR|`ldr r0`|Loads value in the [access context](#access-context) location given by the [L and H registers](#registers) into the register `r0`|

### Arithmetic/Logic instructions
|OP Code (hex)|Instruction|Example|Function in example|
|-|-|-|-|
|7|NOR|`nor r1 r2 r0`|Applies a bitwise nor operation to the values in r1 and r2, puts result into r0|
|8|AND|`and r1 r2 r0`|Applies a bitwise and operation to the values in r1 and r2, puts result into r0|
|9|XOR|`xor r1 r2 r0`|Applies a bitwise xor operation to the values in r1 and r2, puts result into r0|
|A|SHL|`shl r1 r2 r0`|Aplies a bit-left-shift by the value in r2 to r1, puts result into r0|
|B|ADD|`add r1 r2 r0`|Applies an addition to the values in r1 and r2, puts result into r0|
|C|SUB|`sub r1 r2 r0`|Subtracts value in r2 from value in r1, puts result into r0|

### Jump instructions
|OP Code (hex)|Instruction|Example|Function in example|
|-|-|-|-|
|D|JMP|`jmp`|Jumps in program execution to the memory location given by the [L and H registers](#registers)|
|E|JFS|`jfs {FLAG}`|Jumps in program execution to the memory location given by the [L and H registers](#registers) if and only if the bit at the place given by the {FLAG} in the flags register is set|
### Access context instructions
|OP Code (hex)|Instruction|Example|Function in example|
|-|-|-|-|
|F|SAC|`sac`|Sets the [access context](#access-context) according to the [L and H registers](#registers)|

## Optional extensions for AMS
### Implicit value usage
When an operation which requires a register is present, the register can be replaced with an 8-bit integer written in hexadecimal, with the prefix `%`. This just corresponds to the 8-bit integer being used, instead of the value in the register.  
In the compilation process this corresponds to the instruction  
`ldi I [HEX VALUE]`  
being placed in front of the instruction, where the implicit value is used.  
  
***NOTICE:** You can only use **one** implicit value per operation.*