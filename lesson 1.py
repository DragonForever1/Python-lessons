#1
num = int (input())

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

#2

a = int (input())
b = int (input())
c = int (input())

def nod(x, y):
    while y > 0:
        ost = x % y
        x = y
        y = ost
    return x

three_k = 0
max_ar = 0

while c != 0:
    if nod(a, b) < nod(b, c):
        three_k = three_k + 1
        ar = (a + b + c) / 3 
        if ar > max_ar:
            max_ar = ar  
            
    a = b
    b = c
    c = int (input())

if three_k > 0:
    print (three_k, round(max_ar, 2))
else:
    print ("no")
