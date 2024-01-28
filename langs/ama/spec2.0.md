# ⚠️Specification not yet complete⚠️
# Specification for AMA 2.0
## Contents of this specification
## General Information
The "advanced minimalistic assembly", or short AMA, is a programming language with an assembly-like syntax. Saved in .AMA files, programs should usually be "assembled" to an .XAP (eXecutable Assembled Program) file and then be executed by a runtime environment. The language is designed to be light-weight and to have a minimalistic instruction set.  
## Data Storage
### Registers
This language operates on 4 registers, called R0, R1, R2 and R3, of 32 bits each, all initialized as 0. The register R0 holds the index of the current instruction and when written to leads to instruction jumps.  
### Memory
