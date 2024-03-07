# ⚠️SPECIFICATION NOT YET COMPLETE⚠️
# Specification for AMS 2.0
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
|0000|RAM-Block|Reading from this block will result in the [RAM](#ram). Writing to it will write to the [RAM](#ram).|
|0001|Disk access block|This is the block, with which programs are able to access the disk.|
|0002|NUL-Block|Even though not enforced, this block should be kept free for the purpose of easy freeing of other blocks.|
|0003|TMP-Block|This block should be mostly kept free for the purpose of saving important data from the disk access block, when other data is currently being read.|
|0004|CON-Block|This block represents the contents of the console.|
|0005-FFFF|General purpose block|General purpose blocks that can be used as general disk space.|

***NOTICE:** The whole 4GB can't be used as disk space, since 5 * 64KB are required for other purposes.*

## Type syntax
The syntax for the different data types in AMS is listed in the table below.  

|Syntax|Type|
|-|-|
|`r[DIGIT]` / [See register names](#registers)|[Register](#registers)|
|`$[HEX DIGIT][HEX DIGIT]`|8-bit unsigned integer|
|`%[HEX DIGIT][HEX DIGIT]`|[IMPLICIT VALUE](#implicit-value-usage) (Optional)|

## List of instructions
AMS uses a total of 16 instructions with different purposes. These are listed in the tables below.  

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

### Memory instructions
|OP Code (hex)|Instruction|Example|Function in example|
|-|-|-|-|
|4|STR|`str r0`|Stores value in register `r0` into the memory loction given by the [L and H registers](#registers)|
|5|LDR|`ldr r0`|Loads value in the memory location given by the [L and H registers](#registers) into the register `r0`|

### Arithmetic/Logic instructions
|OP Code (hex)|Instruction|Example|Function in example|
|-|-|-|-|
|7|NOR|`nor r0 r1 r2`|Applies a bitwise nor operation to the values in r1 and r2, puts result into r0|
|8|AND|`and r0 r1 r2`|Applies a bitwise and operation to the values in r1 and r2, puts result into r0|
|9|XOR|`xor r0 r1 r2`|Applies a bitwise xor operation to the values in r1 and r2, puts result into r0|
|A|SHL|`shl r0 r1 r2`|Aplies a bit-left-shift by the value in r2 to r1, puts result into r0|
|B|ADD|`add r0 r1 r2`|Applies an addition to the values in r1 and r2, puts result into r0|
|C|SUB|`sub r0 r1 r2`|Subtracts value in r2 from value in r1, puts result into r0|



## Optional extensions for AMS
### Implicit value usage
When an operation which requires a register is present, the register can be replaced with an 8-bit integer written in hexadecimal, with the prefix `%`. This just corresponds to the 8-bit integer being used, instead of the value in the register.  
In the compilation process this corresponds to the instruction  
`ldi I [HEX VALUE]`  
being placed in front of the instruction, where the implicit value is used.  
  
***NOTICE:** You can only use **one** implicit value per operation.*