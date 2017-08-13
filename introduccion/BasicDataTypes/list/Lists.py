class Lists():
    """list wrapper"""
    def __init__(self):
        super(Lists, self).__init__()
        self.list = []

    def insert(self, *args):
        """insert(x,y) insert x at position y(int)"""
        self.list.insert( *args)

    def at(self, *args):
        """object at 'index'"""
        return self.list[args[0]]

    def remove(self, *args):
        """remove first apperece of object """
        self.to_print()
        return self.list.remove(args[0]) 

    def append(self, *args):
        """append(e) insert e at the end of the list"""
        self.list.append(args[0])

    def sort(self, *args):
        """append(e) insert e at the end of the list"""
        self.list = sorted(self.list)

    def pop(self, *args):
        """pop the last element from the list"""
        return self.list.pop()

    def reverse(self, *args):
        """reverse the orden of the list"""
        self.list = sorted(self.list, reverse= True)

    def to_print(self, *args):
        """print the list"""
        print(self.list)
        

