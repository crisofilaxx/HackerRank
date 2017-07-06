if __name__ == '__main__':
    def is_leap(year):
        """HackRank """
        return ((year % 4 == 0 and not year % 100 == 0) or year % 400 == 0)
        
    year = int(input())
    print(is_leap(year))
