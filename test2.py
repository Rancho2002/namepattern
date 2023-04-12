# Python code here
n = int(input())
for i in range(1, n//2+1):
    print('*', end='')
    for j in range(i, n//2+1):
        print(' ', end='')
    print('*', end='')
    print()

if n % 2 == 1:
    print('**')

for i in range(n//2, 0, -1):
    print('*', end='')
    for j in range(i, n//2+1):
        print(' ', end='')
    print('*', end='')
    print()