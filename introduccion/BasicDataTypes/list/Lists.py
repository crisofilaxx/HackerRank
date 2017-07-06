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
        
        

        
