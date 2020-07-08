"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# import the current date and time
today = datetime.now()
print(today)

# count the number of sys.argv arguments
num_args = len(sys.argv)

# store the sys.argv arguments in an array
arguments = sys.argv
print(arguments)

# note: check argv
print(num_args)

#    - if no input
#         print the calendar for the current month
if num_args == 1:
    print(calendar.month(today.year, today.month))
    # cal = calendar.TextCalendar()
    # cal.prmonth(today.year, today.month)
#    - elif one input
#         assume the additional argument is the month and print that month for current year
elif num_args == 2:
    month_num = int(sys.argv[1])
    print(calendar.month(today.year, month_num))
#    - elif two inputs
#         the fist will be the month, 2nd will be the year. We'll use those for the calendar.
elif num_args == 3:
    month_num = int(sys.argv[1])
    year_num = int(sys.argv[2])
    print(calendar.month(year_num, month_num))
#    - else more than 2 inputs
#         send error message
else:
    # print a usage statement
    print("Please provide numerical dates in the following format: 14_cal.py [month] [year]")
    # exit the program
    sys.exit(1)