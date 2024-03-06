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

## Optional extensions for AMS
### Implicit value usage
When an operation which requires a register is present, the register can be replaced with an 8-bit integer written in hexadecimal, with the prefix '%'. This just corresponds to the 8-bit integer being used, instead of the value in the register.  
In the compilation process this corresponds to the instruction  
```ldi I [HEX VALUE]```  
being placed in front of the instruction, where the implicit value is used.  
  
**NOTICE:** You can only use **one** implicit value per operation.