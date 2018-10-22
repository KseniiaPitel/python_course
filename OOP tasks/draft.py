from class_file import File


first = File('C:\python project\\first.txt')
second = File('C:\python project\second.txt')


new_obj = first + second

print(new_obj)
for line in File(new_obj):
    print(line)