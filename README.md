Command line python script called "readme" that, 

when run from any location on the linux filesystem, 

generates a new file in same directory called 
"README_<enclosing_directory>.txt". 

Input:
The script will take as inputs a series of quote enclosed strings as keywords. 

Output
The contents of "README_<enclosing_directory>.txt" will be a YAML containing :

location: <full path of this new readme file>
timestamp: <timestamp when generated>
keywords: <comma separated list of keywords>
files: <all file names in this directory & all sub directories, one per row>

config
The software should have a config file that lets us specify a folder on the system where symlinks to each generated readme file goes.  

Details:
a) Written in Python
b) All development done in Github (if you get the job, first job is to share w/ me)
c) Should be setup for installation via disutils
