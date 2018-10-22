import tempfile
import os


class File:
    def __init__(self, my_file):
        self.my_file = my_file
        self.count = 0

    def __str__(self):
        return self.my_file

    def __iter__(self):
        self.count = 0
        with open(self.my_file, 'r') as f:
            self.result = f.readlines()
        return self

    def __next__(self):
        if self.count < len(self.result):
            res = self.result[self.count]
            self.count += 1
            return res
        else:
            raise StopIteration


for line in File('C:\python project\second.txt'):
    print(line)