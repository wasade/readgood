#!/usr/bin/env python

import sys
from time import sleep
from readgood import state

def _wpm_to_delay(wpm):
    """Convert words per minute to a specific delay"""
    return 60.0 / wpm

def _text_runner(filename):
    """Yield a word at a time"""
    with open(filename) as source:
        for line in source:
            for word in line.split():
                yield word

def driver(filename):
    """Yield the words at the desired rate"""
    words = _text_runner(filename)

    while True:
        sleep(_wpm_to_delay(state.wpm))

        if not state.running:
            sys.exit()
        if state.paused:
            continue

        try:
            word = next(words)
        except StopIteration:
            exit(0)

        yield word
