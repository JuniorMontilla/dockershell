#!usr/bin/env python
#coding: utf-8
#by Junior Montlla

import sys
from subprocess import call
from re import search

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)

call("reset")
printout("Always remember that deleting a container is final!", RED)
print
printout("===================================================", BLUE)
print
printout("===================Login as root===================", BLUE)
print
 
while True:
    try:
        command = raw_input("ϟ ")
        listofcommands = command.split()
    except KeyboardInterrupt:
        print "exit"
        sys.exit(-1)
    try:
        if search("docker", command):
            listofcommands.insert(0,"sudo")
            listofcommands.insert(1,"-i")
            printout("[Good]", GREEN)
            call(listofcommands)
        else:
            call(listofcommands)
    except OSError:
        printout("[Error]:", RED)