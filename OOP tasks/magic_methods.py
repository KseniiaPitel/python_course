import tempfile
import os


class File:
    def __init__(self, my_file):
        self.my_file = my_file
        self.new_obj_path = None

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
            return res.strip("\n")
        else:
            raise StopIteration

    def write(self, *args):
        with open(self.my_file, 'w') as f:
            f.write(*args)

    def get_content(self):
        with open(self.my_file, mode='r') as f:
            return f.read()

    def __add__(self, other):
        self.new_obj_path = os.path.join(tempfile.gettempdir(), 'my_temp_file')
        with open(self.new_obj_path, 'w') as f:
            f.write(self.get_content() + other.get_content())
        new_text = File(self.new_obj_path)
        return new_text


#first = File('C:\python project\\first.txt')
#second = File('C:\python project\second.txt')


#new_obj = first + second

#print(new_obj)

#for line in File('C:\python project\\first.txt'):
#    print(line)