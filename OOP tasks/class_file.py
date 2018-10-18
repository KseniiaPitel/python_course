import tempfile
import os


class File:
    def __init__(self, my_file):
        self.my_file = my_file

    def __str__(self):
        return self.my_file

    def __iter__(self):
        return self

    def __next__(self):
        count = 0
        with open(self.my_file, 'r') as f:
            result = f.readlines()
            count += 1
            if count > len(f.readlines()):
                raise StopIteration
            return result

    def write(self, *args):
        with open(self.my_file, 'w') as f:
            f.write(*args)

    def get_content(self):
        with open(self.my_file, mode='r') as f:
            return f.read()

    def __add__(self, other):
        new_text = File(
            self.get_content() + other.get_content()
        )
        return new_text


first = File('C:\python project\\first.txt')
second = File('C:\python project\second.txt')

new_obj = first + second
new_obj_path = os.path.join(tempfile.gettempdir(), 'my_temp_file')
with open(new_obj_path, 'w') as f:
    f.write(str(new_obj))

for line in File('C:\python project\second.txt'):
    print(line)

# MY CHECKER BLOCK
# print(new_obj)
# print(new_obj_path)

# first.write('test line2\nfirst file')
# second.write('second file test\n')
