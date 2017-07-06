if __name__ == '__main__':
    n = int(input())
    if n % 2 == 0 and (n in list(range(2, 5)) or n > 20):
        print("Not Weird")
    else:
        print("Weird")
        
        
