#1

num = int(input())

del = 1
while del < num:
    del = del * 2

del = del // 2
total = 0

while del > 1:
    if num % del == 0:
        print (del, end=" ")
        total = total + 1 
    del = del // 2  

if total == 0:
    print ("no")

