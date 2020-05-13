Predestinate
============

:Author: David Gay <hello@davidgay.org>

This is a Python wrapper around xautomation.
You can use this to script mouse and keyboard actions in GNU/Linux.

⚠️ This project is no longer maintained. As of 2020, it hasn't been updated
in six or seven years. Use at your own risk.

Requirements
------------

This requires xautomation to be installed.

Installation
------------

You can install Predestinate from PyPI via pip like so::

    pip install predestinate

Usage
-----

Predestinate has been used in my own tests to great effect, and was
implemented on 2013-07-25 to provide mouse movement
with finger motions via the `LEAP Motion controller
<https://www.leapmotion.com/>`_ by a hacker who goes by "dgonyeo".

You can implement Predestinate by taking a quick look at
the code and comments to see what methods you can call. Looking
at ``man xte`` can also be of great use, especially to get the
names of keys. Remember, you *do* need to have ``xautomation``
installed for Predestinate to work.

You can start using Predestinate quite easily like so:

.. code-block:: python

    from predestinate import MouseGod
    mg = MouseGod()
    mg.move(100, 200)
    mg.move(10, 30, relative=True)
    # And much more!

    from predestinate import KeyGod
    kg = KeyGod()
    kg.key_down('Escape')
    # And much more!

License
-------

Predestinate is relased under the GPLv3+ license.
