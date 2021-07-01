'''
A useful python function which can be called from vim (my favourite text editor).

Used to round digits. Very useful when thesis writing!!
'''


import vim
import re

for j in range( vim.current.range.start, vim.current.range.end+1 ) :

    myline = vim.current.buffer[j]
    newline = ""

    for i in myline.split():
        mystr = ""
        try:
            i = float(i)
            mystr = "%.3f" % round(i, 3)
        except ValueError:
            mystr = i
            
        newline += " " + mystr + " "
   
    vim.current.buffer[j] = newline

