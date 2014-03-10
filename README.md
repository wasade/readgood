readgood
========

A speedreader inspired by Spritz and Optimal Recognition Point. This is a dirty hack. 

How to use
==========

You can control the words per minute using 'j' and 'k', and can pause with 'p'. To quit, press 'q'. Keystrokes are monitored in a separate thread, because why not. 

Whats it look like?
===================

It has been awesomized for terminals:

![basic_example][0]

To install
==========

``readgood`` currently depends on [bipy](https://github.com/biocore/bipy) which is unfortunately not ``pip`` installable directly at this time. Additionally, due to dependencies at setup time, ``verman`` and ``numpy`` need to be installed separately. The following should work though (annoying but still simple):

```bash
pip install numpy
pip install git+https://github.com/biocore/bipy.git
pip install verman
pip install readgood
```

[0]: https://github.com/wasade/readgood/raw/master/_assets/example.gif
