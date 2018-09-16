#import sys
#digit_string = sys.argv[1]

digit_string = input("Enter number ")
res_sum = 0
i = 0

if digit_string.isdigit() == True:
    while i < len(digit_string):
        res_sum = res_sum+int(digit_string[i])
        i+=1
    print(res_sum)
else:
    print("not digit")

#from cmd run python.exe solution.py
#this task is verified and passed



