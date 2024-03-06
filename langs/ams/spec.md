# ⚠️SPECIFICATION NOT YET COMPLETE⚠️
# Specification for AMS 2.0
## Contents of this specification
## Introduction
AMS, which is short for "advanced minimalistic assembly", is an 8-bit register-based programming language with an assembly-inspired syntax.  
It is compiled to a special bytecode before being executed by a runtime environment. Alternatively it can be compiled to native machine code or assembly.  
## Data storage
### Registers
AMS uses a total of 8 registers, which are the only directly accessible type of data storage. Most of them have different purposes which are listed in the following table:  
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



## Optional extensions for AMS
### Implicit value usage
When an operation which requires a register is present, the register can be replaced with an 8-bit integer written in hexadecimal, with the prefix `%`. This just corresponds to the 8-bit integer being used, instead of the value in the register.  
In the compilation process this corresponds to the instruction  
`ldi I [HEX VALUE]`  
being placed in front of the instruction, where the implicit value is used.  
  
***NOTICE:** You can only use **one** implicit value per operation.*