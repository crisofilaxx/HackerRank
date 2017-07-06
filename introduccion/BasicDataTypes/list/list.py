if __name__ == '__main__':
    def parse(line): 
        line = line.split()
        typ = ['command', 'first_arg', 'second_arg']
        return dict(zip(typ, line))

    def execute():
        commands = {'insert':, 'print', 'remove', 'append', 'assert', 'sort', 'pop', 'reverse'}
        

    N = int(input())
    the_list = Lista.nueva
    for number_of_commands in range(N):
        line = input()
        command = parse(line)
        execute(command, the_lista)
