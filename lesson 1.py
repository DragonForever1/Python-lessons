#task 1

num = int(input())

p = 1
while p < num:
    p = p * 2

p = p // 2
k = 0

while p > 1:
    if num % p == 0:
        print(p, end=" ")
        k = k + 1 
    p = p // 2  

if k == 0:
    print("NO")

#task 2

