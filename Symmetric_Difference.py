# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
y = input().split(' ')
y = set(y[:x])
w = int(input())
z = input().split(' ')
z = set(z[:w])
a = []
for i in sorted(y.difference(z),key=int):
    a.append(i)
for i in sorted(z.difference(y),key= int):
    a.append(i)
for i in sorted(set(a),key=int):
    print(i)
