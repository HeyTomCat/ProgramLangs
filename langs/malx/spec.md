# !!!SPECIFICATION NOT YET COMPLETE!!!
# Specification for MALX
This specification for the "minimalistic assembly language extended" includes:  
specifications/conventions for files, specification of commands and bit management,  
specification of external commands, specifications of code formatting, error detction/  
correction, management of external commands and specialties.  
## File specifications/conventions  
It should bes saved as an .malx file. This can be made by creating (conventionally) an ASCII .txt file.  
After programming through some sort of text editor the file can be renamed to an .malx file.  
The transpiled byte code (see SPECIALTIES) is saved in an .alc ("assembly language compilation") file.
## Specifications for commands and bit management  
As MALX will mostly be transpiled (see SPECIALTIES) to an intermediate byte code ("assembly language compilation",  
or short ALC), it will need specifications for the usage of all the single bits. This specification is seen in this table,  
where b is short for bit, B for byte and red for redundance and # means its a memory adress, ! means its an unsigned integer,  
$ means its a reference to an operation in the script and / means its the number for an external operation:
|Number|Command|Bit usage|Function|
|-|-|-|-|
|0|add #adr1 #adr2 #adr3|3b cmd, 5b red, 16b adr1, 16b adr2, 16b adr3|5|
|1|sub #adr1 #adr2 #adr3|3b cmd, 5b red, 16b adr1, 16b adr2, 16b adr3|5|
|2|out #adr_from #adr_to|3b cmd, 5b red, 16b adr_from, 16b adr_to|5|
|3|in #adr_from #adr_to|3b cmd, 5b red, 16b adr_from, 16b adr_to|5|
|4|ext /op #arg|3b cmd, 5b red, 16b op, 16b arg|5|
|5|jif $line|3b cmd, 5b red, 16b line|5|
|6|sfig #adr1 #adr2|3b cmd, 5b red, 16b adr1, 16b adr2|5|
|7|sadr #adr !val|3b cmd, 5b red, 16b adr, 32b val|5|  
