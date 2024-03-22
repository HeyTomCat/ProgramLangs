# Specification for Nableq
## Contents of this specification
### [Main Idea](#main-idea-1)
### [Simple IO implementation](#simple-io-implementation-1)
## Main idea
As said in the [description](https://github.com/HeyTomCat/ProgramLangs/blob/main/langs/nableq/DESCRIPTION.md) Nableq is highly inspired by [subleq](https://en.wikipedia.org/wiki/One-instruction_set_computer#Subtract_and_branch_if_less_than_or_equal_to_zero). The idea in subleq is to have just one instruction:  
`subleq a b c`  
`a`, `b` and `c` are memory addresses, with the program being loaded into RAM in the beginning and the instruction does the following:  
  
1.Subtracts value in `b` from value in `a`. Result is put into `a`.  
  
2.If the result was less than or equal to `0`, the execution continues at address `c`.  
  
With Nableq the only change is applying a bitwise NAND operation instead of a subtraction. So the execution scheme for Nableq looks like this:  
  
1.Applys a bitwise NAND operation to the value in `a` and the value in `b`. Result is put into `a`.   
  
2.If the result was less than or equal to `0`, the execution continues at address `c`.  
## Simple IO / Halt implementation
