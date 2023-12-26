# Specification for MALX
This specification for the "minimalistic assembly language extended" includes:  
specifications/conventions for files, specification of commands and bit management,  
specification of external commands, specifications of code formatting, corruption detection/  
correction, management of external commands and specialties.  
## File specifications/conventions  
It should bes saved as an .malx file. This can be made by creating (conventionally) an ASCII .txt file.  
After programming through some sort of text editor the file can be renamed to an .malx file.  
The transpiled byte code (see SPECIALTIES) is saved in an .ALC ("assembly language compilation") file.
## Specifications for commands and bit management  
As MALX will (in most cases) be transpiled (see SPECIALTIES) to an intermediate byte code ("assembly language compilation",  
or short ALC), it will need specifications for the usage of all the single bits. This specification is seen in this table,  
where b is short for bit, B for byte, cmd for the command and red for redundance and # means its a memory adress,  
! means its an unsigned integer, $ means its a reference to an operation in the script and / means its the number for an external operation:
|Number|Command|Bit usage|Total|Function|
|-|-|-|-|-|
|0|add #adr1 #adr2 #adr3|3b cmd, 5b red, 16b #adr1, 16b #adr2, 16b #adr3|7B|Adds values in #adr1 and #adr2. Result is put into #adr3.|
|1|sub #adr1 #adr2 #adr3|3b cmd, 5b red, 16b #adr1, 16b #adr2, 16b #adr3|7B|Subtracts values in #adr1 and #adr2. Result is put into #adr3.|
|2|out #adr_from #adr_to|3b cmd, 5b red, 16b #adr_from, 16b #adr_to|5B|Outputs all the values from #adr_from to #adr_to as UTF-32 characters WITHOUT NEW LINES.|
|3|in #adr_from #adr_to|3b cmd, 5b red, 16b #adr_from, 16b #adr_to|5B|Takes UTF-32 input, puts into adresses from #adr_from to #adr_to. Further input will be ignored.|
|4|ext /op #arg|3b cmd, 5b red, 16b /op, 16b #arg|5B|Executes external /op with value in #arg as argument (see MANAGEMENT OF EXTERNAL COMMANDS). Operations from 0-255 are system-/language-reserved (see SPECIFICATION OF EXTERNAL COMMANDS).|
|5|jif $line|3b cmd, 5b red, 16b $line|3B|Jumps to $line if global flag is set.|
|6|sfig #adr1 #adr2|3b cmd, 5b red, 16b #adr1, 16b #adr2|5B|Sets global flag if value in #adr1 is greater than value in #adr2. Else resets flag.|
|7|sadr #adr !val|3b cmd, 5b red, 16b #adr, 32b !val|7B|Sets value of #adr to !val.|  
## Specification of external commands  
|Number|Command|Function|
|-|-|-|
|0|halt|Ends program with argument as exit status code.|
|1|wait|Waits for an amount of milliseconds. Amount is given by argument|  

No further system-/language-reserved external commands existent yet.
## Specifications of code formatting
In any line, if theres a \, behind that \ is a comment which should be ignored by com-/transpilers or interpreter.
Singular commands are always seperated by a ; and a optionaly a new line, which might helps com-/transpilers or interpreters.  
Additionally all numbers should be typed in hexadecimal. The requirement of these ideas should be enforced by your  
com-/transpilers or interpreters to help with the upkeeping of a common MALX syntax to not need multiple versions. Your  
com-/transpiler or interpreter should also output a warning if it is tried to set memory address #0. The reason for this  
can be read in MANAGEMENT OF EXTERNAL COMMANDS.  
## Corruption detection/correction  
In the transpiled .alc format (see SPECIALTIES) there are 5 redundant bits per command. These can be used for error  
detection and/or minor error correction. The transpiled command size can be 3, 5 or 7 bytes depending on the command.  
The 5 bits will be copys of 5bits through out the command transpilation, ignoring the redundant bits themselves, so  
either 19 (2B, 3b), 51 (4B, 3b) or 83 bits (6B, 3b). In the following table Command Transpilation Size (CTS) and the  
Redundancy Copy Indexes starting at 0, ignoring the redundant bits themselves (RCIs) are listed:  
|CTS|RCIs|
|-|-|
|3B|0, 4, 8, 12, 16|
|5B|0, 11, 22, 33, 44|
|7B|0, 17, 34, 51, 68|  

If a bit isn't equal to its redundant copy, replace the bit with the copy. If 3 or more copys don't correspond to the bit,  
its more likely, that because the reundants are stored in batches, they are corrupted so instead change the redundant copy  
to the corresponding bit. Even with this simple corruption correction a warning of possible corruption should still be outputed  
if any bit isn't equal to its redundant copy.  
## Management of external commands
All external commands from 0 to 255 are system reserved, but from 256 to 65535 are user defined (see SPECIFICATIONS FOR COMMANDS  
AND BIT MANAGEMENT). These user defined external commands will be defined and saved in a COMMANDS.EXT (external) file. In this file every  
external command is saved as a line, structured like this:  
[Number of command]-[Path to executable];  
Lines may only be structured like this. No comments, empty lines or "compression" of multiple commands into one line should be  
allowed. The file the path is pointing to may be a .MALX file, a .ALC file or any system executable. In the case of a .MALX or .ALC  
the argument will be written into memory address #0. In case of a system executable the argument will be given as a single UTF-32 character  
in the arguments.
## Specialties
Before this language is executed it will (in most cases) be compiled to an intermediate byte code as an .ALC ("assembly language compilation") file.  
This byte code also has a small corruption detection/correction algorithm (see CORRUPTION DETECTION/CORRECTION). Most of the commands won't be  
in the language itself, but will be loaded through external commands (see SPECIFICATION OF EXTERNAL COMMANDS, MANAGEMENT OF EXTERNAL COMMANDS).
