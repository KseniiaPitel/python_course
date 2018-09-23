key_val_dict = dict ()


key = int (input("key "))
val = input("val ")

key_val_dict.update({key:val})
dict_for_file = str(key_val_dict)

#print(type(key_val_dict))
#print(key_val_dict)
f = open('test.txt', 'a')
f.write(dict_for_file)
f.close()

f = open('test.txt', 'r')
print(f.read())