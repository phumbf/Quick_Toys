'''
A useful python function which can be called from vim (my favourite text editor).

Used to convert scientific notation, spat out from my programs, into decimal notation 
for when writing up
'''

import vim
import re

for i in range( vim.current.range.start, vim.current.range.end+1 ) :

    myline = vim.current.buffer[i]

    mymatch = re.search( '(\d+\.\d+e[+-]\d+)', myline )
    while mymatch :

        span = mymatch.span()
        scirep = mymatch.groups()[0]
        decrep = '%.2f' % float(scirep)

        myline = myline[:span[0]] + decrep + myline[span[1]:]

        mymatch = re.search( '(\d+\.\d+e[+-]\d+)', myline )


    vim.current.buffer[i] = myline

