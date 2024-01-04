# Version Formatting  
The version numbers are formatted like this:  
v[main-version].[variation-version]  
## The main version
If the main version is 0 the specification has not yet been completed.  
1 means it has been completed and 2 or higher means there were several  
overworks. Each overwork adds 1 to the main version.  
## The variation version
If the variation version is 0 it means it's the first version of the  
current main version. Every variation version after that adds some  
minor changes.  
## The changelogs
Most variation versions also comes with a small changelog. This can be  
found (in the directory of the programming language) in the subdirectory  
changelogs-v[main-version]. There its in the file  
changelog-v[main-version].[variation-version].md  
For example the changelog for MALX v1.1 can be found in  
langs/malx/changelogs-v1/changelog-v1.1.md.  
But there are exeptions:  
-First versions (variation version 0) come without a  
   changelog.  
-Incomplete versions (main version 0) come without a  
   changelog.  
