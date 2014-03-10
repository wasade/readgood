#!/usr/bin/env python

from functools import partial
from types import GeneratorType
from readgood import state
from readgood.util import RingBuffer
from readgood.workflow import ReadGooder
from pyqi.core.command import (Command, CommandIn, CommandOut,
    ParameterCollection)


class ReadGooderCommand(Command):
    BriefDescription = "Read gooder"
    LongDescription = "Put all the words in a box"
    CommandIns = ParameterCollection([
        CommandIn(Name='text', DataType=str,
                  Description='The input text', Required=True),
        CommandIn(Name='tickmark_in_box_index', DataType=int,
                  Description='The tick position of the box',
                  Required=False, Default=8),
        CommandIn(Name='buffer_size', DataType=int,
                  Description='Ring buffer size', Default=100),
        CommandIn(Name='box_width', DataType=int,
                  Description='Length of the box', Default=20)
    ])

    CommandOuts = ParameterCollection([
        CommandOut(Name="orp_word", DataType=GeneratorType,
                   Description="Resulting formatted words"),
    ])

    def _boxify_callback(self, box_width, tick_pos, wk):
        """Put a box on it"""
        # this should be pushed to the output handler
        dash = u'\u2500'
        downtick = u'\u252c'
        uptick = u'\u2534'

        left = dash * tick_pos
        right = dash * (box_width - tick_pos - 1)

        up = left + downtick + right
        down = left + uptick + right

        return "%s\n%s\n%s" % (up, wk.state['formatted'], down)

    def run(self, **kwargs):
        text = kwargs.pop('text')
        box_width = kwargs.pop('box_width')
        tickpos = kwargs['tickmark_in_box_index']
        ring_size = kwargs.pop('buffer_size')

        state.ringbuffer = RingBuffer(ring_size)
        success_f = partial(self._boxify_callback, box_width, tickpos)

        wf = ReadGooder({}, options=kwargs)
        iter_ = wf(text, success_callback=success_f)

        return {'orp_word': iter_}

CommandConstructor = ReadGooderCommand
