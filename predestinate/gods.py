import subprocess # to run xautomation


class XGod(object):
    """Base class for all god objects."""

    def __init__(self):
        pass

    def usleep(self, i):
        """Wait for i microseconds"""
        self.xte_args = "usleep {}".format(i)
        subprocess.call(["xte", self.xte_args])


class MouseGod(XGod):
    """Can predestine the actions of the mouse."""

    def __init__(self, *args, **kwargs):
        super(MouseGod, self).__init__(*args, **kwargs)

    def move(self, x, y, relative=False):
        """Move the mouse pointer. Default is absolute coords.
        x: change in x
        y: change in y
        relative: move mouse relative to its current position"""
        if not relative:
            self.xte_args = "mousemove {} {}".format(x, y)
            subprocess.call(["xte", self.xte_args])
        else:
            self.xte_args = "mousermove {} {}".format(x, y)
            subprocess.call(["xte", self.xte_args])

    def click(self, i):
        """Click a mouse button.
        i: the number of the button to press
            1 - left mouse
            2 - middle mouse
            3 - right mouse"""
        self.xte_args = "mouseclick {}".format(i)
        subprocess.call(["xte", self.xte_args])

    def click_down(self, i):
        """Press mouse button i down"""
        self.xte_args = "mousedown {}".format(i)
        subprocess.call(["xte", self.xte_args])

    def click_up(self, i):
        """Release mouse button i"""
        self.xte_args = "mouseup {}".format(i)
        subprocess.call(["xte", self.xte_args])


class KeyGod(XGod):
    """Can predestine the actions of the keyboard."""

    def __init__(self):
        super(KeyGod, self).__init__(*args, **kwargs)

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

    def key_str(self, string):
        """Press and release each character in the string
        string: the string of characters to press and release"""
        self.xte_args = "str {}".format(string)
        subprocess.call(["xte", self.xte_args])
