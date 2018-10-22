<<<<<<< HEAD
from class_file import File


first = File('C:\python project\\first.txt')
second = File('C:\python project\second.txt')
=======
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
>>>>>>> origin/master


new_obj = first + second

print(new_obj)
for line in File(new_obj):
    print(line)