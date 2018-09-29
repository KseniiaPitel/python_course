import sys
stairs_num=sys.argv[1]
#stairs_num = input("Enter the number of stairs ")
stairs_num = int(stairs_num)
hashtags = (stairs_num + 1) - stairs_num
spaces = stairs_num - 1

n: int = spaces
j: int = 1
hash = "#"
sp = " "
temp_sp = sp * n
temp_hash = hash * j

while hashtags <= n and spaces >= j:
    print(temp_sp+temp_hash)
    n -= 1
    j += 1
    temp_sp = sp * n
    temp_hash = hash * j
print(hash*stairs_num)

