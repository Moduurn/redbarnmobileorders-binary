
EXE file to pull daily Moduurn mobile orders for registered Redbarn stores. If optional arguments are not passed it will get the data for current day in the current folder.

Usage : moduurnorders --savefolder={destinationfolder} --searchdate={date in YYYY-MM-DD format}. 

optional arguments  : --savefolder can be used to specify the destination folder
                      --searchdate   to get the extract for any given dates 

example: 

moduurnorders --savefolder=./extract --searchdate=2022-03-03

This command will extract Moduurn Mobile Orders completed on 2022-03-03 into folder extract. 

 