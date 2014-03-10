#!/usr/bin/env python

import tty
import sys
import termios

stdin = sys.stdin
stdin_fd = sys.stdin.fileno()
stdin_settings = termios.tcgetattr(stdin_fd)

class RingBuffer(list):
    """A basic ring, or cyclic buffer"""
    def __init__(self, maxsize, *args, **kwargs):
        self.maxsize = maxsize
        super(RingBuffer, self).__init__(*args, **kwargs)

    def append(self, item):
        if len(self) >= self.maxsize:
            self.pop(0)
        super(RingBuffer, self).append(item)


def stdin_reset():
    """Reset the terminal"""
    termios.tcsetattr(stdin_fd, termios.TCSADRAIN, stdin_settings)

def getch():
    """Get a char, derived from http://code.activestate.com/recipes/134892/"""
    try:
        tty.setcbreak(stdin_fd)
        ch = stdin.read(1)
    except (KeyboardInterrupt, SystemExit):
        stdin_reset()
    stdin_reset()
    return ch
