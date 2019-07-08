class Backpack:
    """A Backpack object class. Has a name, a color,
    a list of contents and its max size
    Attributes:
        name(str) - the name of the backpack's owner;
        color(str) - color of the backpack;
        contents(list) - the contents of the backpack;
        max_size(int) - max size of the backpack.
    """
    def __init__(self, name, color, max_size = 5):
        """
        Set the name, color and max_size (has default value 5).


        Parameters:
            name(str) - the name of the backpack's owner;
            color(str) - color of the backpack;
            max_size(int) - max size of the backpack.
        """
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []
    def put(self, item):
        """
        Add 'item' to the backpack's list of contents.
        """
        if len(self.contents) >= self.max_size:
            print('No room!')
        else:
            self.contents.append(item) # Use 'self.contents', not just 'contents'.
    def take(self, item):
        """
        Remove 'item' from the backpack's list of contents.
        """
        self.contents.remove(item)
    def dumb(self):
        """
        Reset the contents of list.
        """
        self.contents.clear()
