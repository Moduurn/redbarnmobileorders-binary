
EXE file to pull the mobile orders from Moduurn Stores. You may use the command  moduurnorders --savefolder=.{destinationfolder} --searchdate={date in YYYY-MM-DD format}   to pull the mobile orders for a given day. 
If optional arguments are not passed it will get the data for current day.

File Name : moduurnorders.exe 
optional arguments  : --savefolder can be used to specify the destination folder
                      --searchdate   to get the extract for any given dates 

example: 

moduurnorders --savefolder=./extract --searchdate=2022-03-03