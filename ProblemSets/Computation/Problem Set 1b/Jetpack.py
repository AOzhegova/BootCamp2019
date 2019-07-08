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
