# Enter your code here. Read input from STDIN. Print output to STDOUT

count = list(map(int,input().strip().split()))
m = count[0]
n = count[1]
Arr = list(map(int,input().strip().split()))
A = set(map(int,input().strip().split()))
B = set(map(int,input().strip().split()))
happy = 0
for i in Arr:
    if i in A : happy = happy + 1
    elif i in B : happy = happy - 1
print (happy)
