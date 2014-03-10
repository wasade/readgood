#!/usr/bin/env python
from __future__ import division

__credits__ = []

from pyqi.core.interfaces.optparse import (OptparseUsageExample,
                                           OptparseOption, OptparseResult)
from pyqi.core.command import (make_command_in_collection_lookup_f,
                               make_command_out_collection_lookup_f)
from readgood.commands.readgooder import CommandConstructor
from readgood.interfaces.optparse.input_handler import driver
from readgood.interfaces.optparse.output_handler import box_writer

# Convenience function for looking up parameters by name.
cmd_in_lookup = make_command_in_collection_lookup_f(CommandConstructor)
cmd_out_lookup = make_command_out_collection_lookup_f(CommandConstructor)

# Examples of how the command can be used from the command line using an
# optparse interface.
usage_examples = [
    OptparseUsageExample(ShortDesc="Write all the text",
                         LongDesc="Read gooder",
                         Ex="%prog --text=some_file")
]

inputs = [
    OptparseOption(Parameter=cmd_in_lookup('tickmark_in_box_index'),
                   Type=int,
                   Action='store', # default is 'store', change if desired
                   ShortName=None, # must be defined if desired
                   ),
    OptparseOption(Parameter=cmd_in_lookup('text'),
                   Type=str,
                   Action='store',
                   Handler=driver
                   ),
    OptparseOption(Parameter=cmd_in_lookup('box_width'),
                   Type=int,
                   Action='store', # default is 'store', change if desired
                   ShortName=None, # must be defined if desired
                   ),
    OptparseOption(Parameter=cmd_in_lookup('buffer_size'),
                   Type=int,
                   Action='store', # default is 'store', change if desired
                   ShortName=None, # must be defined if desired
                   )
]

outputs = [
    OptparseResult(Parameter=cmd_out_lookup('orp_word'),
                    Handler=box_writer, # must be defined
                    InputName=None), # define if tying to an OptparseOption
]
