#!/usr/bin/env python

import sys
from readgood import state

def box_writer(result_key, data, option_value=None):
    """Write the text!"""
    n_output_lines = 4
    print "\n" * n_output_lines,
    for item in data:
        sys.stdout.write('\x1b[1A\x1b[2K' * n_output_lines)  # shift the back
        sys.stdout.write(item)
        sys.stdout.write('\n')
        sys.stdout.write("WPM: %d\n" % state.wpm)
