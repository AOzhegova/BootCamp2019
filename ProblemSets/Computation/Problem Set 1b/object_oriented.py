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
    def __add__(self, other):
        """
        Add the number of contents of each Backpack.
        """
        return len(self.contents) + len(other.contents)
    def __lt__(self, other):
        """If 'self' has fewer contents than 'other', return True.
        Otherwise, return False.
        """
        return len(self.contents) < len(other.contents)
    def __eq__(self, other):
        """
        Compare two objects by the name, the color and
        the number of contents
        """
        return self.name == other.name and \
            self.color == other.color and \
           len(self.contents == len(other.contents))
    def __str__(self):
        """
        Returns the string representation of an object
        """
        return "Owner:" + self.name + "   " + "Color:" + self.color + \
        "  " + "Size:" + str(len(self.contents)) + "  " + "Max Size:" + \
         str(self.max_size) + "  " + "Contents:" + str(self.contents)



class Jetpack(Backpack):
    """A Jetpack object class. Has a name, a color, a fuel
    a list of contents, and its max size
    Attributes:
        name(str) - the name of the backpack's owner;
        color(str) - color of the backpack;
        fuel(int);
        contents(list) - the contents of the backpack;
        max_size(int) - max size of the backpack.
    """
    def __init__(self, name, color, max_size = 2, fuel = 10):
        """
        Set the name, color and max_size (has default value 5).


        Parameters:
            name(str) - the name of the backpack's owner;
            color(str) - color of the backpack;
            fuel(int);
            max_size(int) - max size of the backpack.
        """
        self.name = name
        self.color = color
        self.max_size = max_size
        self.fuel = fuel
        self.contents = []
        Backpack.__init__(self, name, color, max_size)
    def fly(self):
        """
        Decrement the amount of fuel
        """
        if self.fuel > 1:
            self.fuel = self.fuel - 1
        else:
            print('Not enough fuel!')
    def dumb(self):
        """
        Reset the contents of list and empty fuel.
        """
        self.contents.clear()
        self.fuel = 0
