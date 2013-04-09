import subprocess # to run xautomation


class MouseGod(object):
    """Can predestine the actions of the mouse."""

    @classmethod
    def move_mouse_abs(cls, x, y):
        """Move the mouse pointer absolutely
        x: change in x
        y: change in y"""
        xte_command = "mousemove {} {}".format(x, y)
        subprocess.call(["xte", xte_command])

    @classmethod
    def move_mouse_rel(cls, x, y):
        """Move the mouse pointer relatively
        x: change in x
        y: change in y
        (values can be negative)"""
        xte_command = "mousermove {} {}".format(x, y)
        subprocess.call(["xte", xte_command])
