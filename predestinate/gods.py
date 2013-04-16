import subprocess # to run xautomation


class MouseGod(object):
    """Can predestine the actions of the mouse."""

    def __init__(self):
        pass

    def move_mouse_abs(self, x, y):
        """Move the mouse pointer absolutely.
        x: change in x
        y: change in y"""
        self.xte_args = "mousemove {} {}".format(x, y)
        subprocess.call(["xte", self.xte_args])

    def move_mouse_rel(self, x, y):
        """Move the mouse pointer relatively.
        x: change in x
        y: change in y
        (values can be negative)"""
        self.xte_args = "mousermove {} {}".format(x, y)
        subprocess.call(["xte", self.xte_args])


class KeyGod(object):
    """Can predestine the actions of the keyboard."""

    def __init__(self):
        pass

    def key(self, key):
        """Press and release a key.
        key: a string representing the key to press and release"""
        self.xte_args = "key {}".format(key)
        subprocess.call(["xte", self.xte_args])

    def key_down(self, key):
        """Press a key down.
        key: a string representing the key to press"""
        self.xte_args = "keydown {}".format(key)
        subprocess.call(["xte", self.xte_args])

    def key_up(self, key):
        """Release a key.
        key: a string representing the key to release"""
        self.xte_args = "keyup {}".format(key)
        subprocess.call(["xte", self.xte_args])
