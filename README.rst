Predestinate
============

:Author: David Gay <oddshocks@riseup.net>

Python wrapper around xautomation because Python is disco super-fly.
You can use this to script mouse and keyboard actions in GNU/Linux.

Requirements
------------

This requires xautomation to be installed (duh this is a wrapper don't
be a goofball).

Installation
------------

You can install Predestinate from PyPI via pip like so::

    pip install predestinate

**WARNING:** I have just discovered what may be a fatal bug which
prevents installation via pip due to improper implementation of
our distribute setup support. I am working on this ASAP, and have
a ticket open: https://github.com/oddshocks/pythong/issues/19/.

Usage
-----

Predestinate has been used in my own tests to great effect, and was
just implemented tonight (2013-07-25) to provide mouse movement
with finger motions via the `LEAP Motion controller
<https://www.leapmotion.com/>`_ by a hacker who goes by "dgonyeo".

I'd like to spend more time on documentation and whatnot, but am
under the weight of other projects at the moment. I *can* tell you
that you can implement it quite easily by taking a quick look at
the code and comments to see what methods you can call. Looking
at ``man xte`` can also be of great use, especially to get the
names of keys. Remember, you *do* need to have ``xautomation``
installed for Predestinate to work.

You can start using Predestinate quite easily like so:

.. code-block:: python

    from predestinate import MouseGod
    mg = MouseGod()
    mg.move(100, 200) # And much more!

    from predestinate import KeyGod
    kg = KeyGod()
    kg.key('Escape') # And much more!


I'll be expanding this documentation much more in the future,
especially as I complete my summer internship. Thanks for
checking it out! Feel free to ask questions and open tickets
for bugs and feature requests. I appreciate it. :)

License
-------

Predestinate is relased under the GPLv3+ license.
