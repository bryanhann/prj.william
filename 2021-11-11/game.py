#!/usr/bin/env python3
from dochelp import *

# Define three kinds of pieces: Frog, Toad, and Empty

F = "FROG"
T = "TOAD"
E = "----"

# Define the board we will play with

BOARD=[ F, F, E, E, E, T, T ]


DOC=f"""

---------------------------------------------------------
Welcome to the game "Frogs vs Toads" !
---------------------------------------------------------

We start with a board:

    {BOARD}

This board is a {list_} of {len(BOARD)} items.  Each item is a {string_}
of {len(E)} characters.  Each string in the list represents a piece:

    The string "{F}" represents a frog.
    The string "{T}" represents a toad.
    The string "{E}" represents an empty space.

From the player's point of view, there are only two kinds of pieces
to consider: frogs and toads.  But from our point of view as game
developers, we will use the string "{E}" to represent a special
piece called 'empty' which represents a position on the board
that is empty.
"""

print(DOC)
