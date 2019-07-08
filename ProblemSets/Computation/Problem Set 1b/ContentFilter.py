class ContentFilter:
    def __init__(self, name):
        FileOpen = False
        self.name = name
        while not FileOpen:
            try:
                myFile = open(self.name, 'r')
            except FileNotFoundError:
                input('File name is invalid. Please, try once again.')
            except TypeError:
                input('File name is invalid. Please, try once again.')
            except OSError:
                input('File name is invalid. Please, try once again.')
            else:
                FileOpen = True
        self.contents = myFile.readlines()
        cont = ""
        for line in self.contents:
            cont = cont + line
        self.contents = cont
        myFile.close()
