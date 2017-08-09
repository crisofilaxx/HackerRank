import Lists

if __name__ == '__main__':
    def parse(line): 
        line = line.split()
        typ = ['command', 'first_arg', 'second_arg']
        return dict(zip(typ, line))

    def execute(command, the_list):
        commands = {'insert'  : the_list.insert,
                    'print'   : the_list.to_print,
                    'remove'  : the_list.remove,
                    'append'  : the_list.append,
                    'assert'  : the_list.assert,
                    'sort'    : the_list.sort,
                    'pop'     : the_list.pop,
                    'reverse' : the_list.reverse}
        

    N = int(input())
    the_list = Lists()
    for number_of_commands in range(N):
        line = input()
        command = parse(line)
        execute(command, the_list)
