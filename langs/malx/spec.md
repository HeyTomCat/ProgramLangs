# !!!SPECIFICATION NOT YET COMPLETE!!!
# Specification for MALX
This specification for the "minimalistic assembly language extended" includes:  
specifications/conventions for files, specification of commands and bit management,  
specification of external commands, specifications of code formatting, specialties.  
## File specifications/conventions  
It should bes saved as an .malx file. This can be made by creating (conventionally) an ASCII .txt file.  
After programming through some sort of text editor the file can be renamed to an .malx file.  
The transpiled
## Specifications for commands and bit management  
As MALX will mostly be transpiled to an intermediate byte code ("minimalistic assembly compilation", or short MAC),
it will need specifications for the usage of all the single bits.
|Number|Command|Byte usage|Function|
|-|-|-|-|
|0|add #adr1 #adr2 #adr3|3bit cmd, 5bit redundance,|5|
|1|sub #adr1 #adr2 #adr3|3bit cmd, 5bit redundance,|5|
|2|out #adr_from #adr_to|3bit cmd, 5bit redundance,|5|
|3|in #adr_from #adr_to|3bit cmd, 5bit redundance,|5|
|4|ext /op #arg|3bit cmd, 5bit redundance,|5|
|5|jif $line|3bit cmd, 5bit redundance,|5|
|6|sfig #adr1 #adr2|3bit cmd, 5bit redundance,|5|
|7|sadr #adr !val|3bit cmd, 5bit redundance,|5|
