#!/usr/bin/env python

import unicodedata
from bipy.core.workflow import Workflow, not_none
from numpy import floor, ceil

class ReadGooder(Workflow):
    """Help people read gooder"""
    def initialize_state(self, item):
        self.state = {'word': item,
                      'orp_idx': None,
                      'orp_word': None,
                      'formatted': None}

    @Workflow.method(priority=100)
    def strip_nasty_characters(self):
        """Drop the nasty"""
        self.state['word'] = self.state['word'].strip().decode('utf-8')

    @Workflow.method(priority=90)
    def determine_orp(self):
        """Hackishly determine the optimal recognition point"""
        word = self.state['word']
        if len(word) == 2:
            orp = 2
        elif len(word) <= 5:
            orp = ceil(len(word) / 2.0).astype(int)
        elif len(word) % 2:
            orp = floor(len(word) / 2.0).astype(int)
        else:
            orp = len(word) / 2
        self.state['orp_idx'] = orp - 1

    @Workflow.method(priority=80)
    def inject_red_ascii(self):
        """Mark a letter red"""
        word = self.state['word']
        orp_idx = self.state['orp_idx']

        left = word[:orp_idx]
        orp = "%s%s%s" % ('\033[91m', word[orp_idx], '\033[0m')
        right = word[orp_idx+1:]

        self.state['orp_word'] = ''.join([left, orp, right])

    @Workflow.method(priority=70)
    @Workflow.requires(option='tickmark_in_box_index', values=not_none)
    def justify_word(self):
        """Justify the word with respect to a tickmark location"""
        tickmark = self.options['tickmark_in_box_index']
        orp_idx = self.state['orp_idx']
        orp_word = self.state['orp_word']

        left_pad = tickmark - orp_idx
        self.state['formatted'] = ''.join([' ' * left_pad, orp_word])
