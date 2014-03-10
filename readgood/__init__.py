#!/usr/bin/env python

import sys
import atexit
import threading
from .util import stdin_reset, getch
from verman import Version

readgood_version = Version("readgood", 0, 1, 1, releaselevel="dev",
                           init_file=__file__)
__version__ = readgood_version.mmm


class state(object):
    """Hold global state"""
    wpm = 100
    paused = 0
    running = True


def cleanup():
    """Exit cleanly"""
    stdin_reset()
    print '\033[2K'  # reset the cursor


def start_keystroke_thread():
    """Kick off the keystroke monitoring thread"""
    t = threading.Thread(target=keystroke)
    t.daemon = True
    t.start()


def _pause():
    """Toggle paused"""
    state.paused = 1 - state.paused


def _wpm_f(v):
    """Update words per minute"""
    def f():
        state.wpm += v
        if state.wpm <= 5:
            state.wpm = 5
        elif state.wpm >= 1000:
            state.wpm = 1000
    return f


def noop():
    pass


def die():
    """Update state if we die"""
    state.running = False
    sys.exit()


# what to do with a key press
key_map = {'q': die,
           'j': _wpm_f(-5),
           'k': _wpm_f(5),
           'p': _pause}


def _handle_key_press(key):
    """Handle a key"""
    key_map.get(key, noop)()


def keystroke():
    """Process keystrokes as they happen"""
    while True:
        ch = getch()
        _handle_key_press(ch)

start_keystroke_thread()
atexit.register(cleanup)
