class Lists():
    """list wrapper"""
    def __init__(self):
        super(Lists, self).__init__()
        self.list = []

    def insert(self, x, y):
        """insert(x,y) insert x at position y(int)"""
        self.list.insert(y, x)

    def at(self, index):
        """object at 'index'"""
        return self.list[index]

    def remove(self, element):
        """remove first apperece of object """
        return self.list.remove(element) 

    def append(self, element):
        """append(e) insert e at the end of the list"""
        self.list.append(element)

    def sort(self):
        """append(e) insert e at the end of the list"""
        self.list = sorted(self.list)

    def pop(self):
        """pop the last element from the list"""
        return self.list.pop()

    def reverse(self):
        """reverse the orden of the list"""
        self.list = sorted(self.list, reverse= True)

