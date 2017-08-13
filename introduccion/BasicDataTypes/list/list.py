from Lists import Lists as lst

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
    the_list = lst()
    for number_of_commands in range(N):
        line = input()
        command = parse(line)
        execute(command, the_list)
