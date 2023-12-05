#!/usr/bin/env python3
from mycolors import red, green

FROG=red("FROG")
TOAD=green("TOAD")
NONE="----"

BOARD=[ FROG, FROG, NONE, NONE, NONE, TOAD, TOAD ]

def board():
    aa = '|' . join(BOARD)
    bb = '[' + aa + ']'
    return bb
print( red('sss') )

print( green('sss') )
print( '|'.join(BOARD) )
print(board())

