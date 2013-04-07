import subprocess # to run xautomation


class XMouseGod(object):
    """Can predestine the actions of the mouse."""

    @classmethod
    def move_mouse_abs(cls, x, y):
        """Move the mouse pointer absolutely
        x: change in x
        y: change in y"""
        subprocess.call(['xte', "xmousemove", str(x), str(y), "'"])

    @classmethod
    def move_mouse_rel(cls, x, y):
        """Move the mouse pointer relatively
        x: change in x
        y: change in y
        (values can be negative)"""
        subprocess.call(["xte", "'xmousermove", str(x), str(y), "'"])
