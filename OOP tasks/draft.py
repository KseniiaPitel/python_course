class File:
    def __init__(self, my_file):
        self.my_file = my_file

    def __iter__(self):
        return self

    def __next__(self):
        count = 0
        with open(self.my_file, 'r') as f:
            for line in f.readlines():
                return line

            if count > sum(1 for _ in f):
                raise StopIteration




print(next(File('C:\python project\second.txt')))
#for line in File('C:\python project\second.txt'):
#    print(line)

