if __name__ == '__main__':
    def print_n(number):
        s = ''
        for seq in range(1, number+1):
            s += str(seq)
        print(s)
    
    n = int(input())
    print_n(n)

