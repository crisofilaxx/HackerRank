
if __name__ == '__main__':
    def parse(line): 
        line = line.split()
        typ = ['command', 'first_arg', 'second_arg']
        for arg in range(1,3):
            if len(line) >= arg+1:
                line[arg] = int(line[arg])
            else:
                line.append("EMPTY")
            
        return dict(zip(typ, line))

    def execute(command, the_list):
        commands = {'insert'  : the_list.insert,
                    'print'   : the_list.to_print,
                    'remove'  : the_list.remove,
                    'append'  : the_list.append,
                    'sort'    : the_list.sort,
                    'pop'     : the_list.pop,
                    'reverse' : the_list.reverse}
        commands[command['command']](command['first_arg'],command['second_arg'])
        

    N = int(input())
    the_list = Lst()
    for number_of_commands in range(N):
        line = input()
        command = parse(line)
        execute(command, the_list)




class Lst():
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
        

