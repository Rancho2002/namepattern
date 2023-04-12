def A(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or j == 0 or j == n-1 or i == n//2):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def B(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 and j != n-1 or j == 0 or i == n-1 and j != n-1 or i != 0 and i != n-1 and j == n-1 and i != n//2 or i == n//2 and j != n-1):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def C(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or j == 0 or i == n-1):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def D(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 and j != n-1 or j == 0 or i == n-1 and j != n-1 or i != 0 and i != n-1 and j == n-1):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def E(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or j == 0 or i == n//2 or i == n-1):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def F(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or j == 0 or i == n//2):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def G(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or j == 0 or i == n-1 and j < n//2 or j == n//2 and i >= n//2 or i == n//2 and j > n//2 or j == n-1 and i > n//2):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def H(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (j == 0 or j == n-1 or i == n//2):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def I(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n-1 or j == n//2):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def J(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or j==n//2 or i==n-1 and j<n//2 or j==0 and i>=n//2):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def K(point: str, n: int) -> None:
    for i in range(1, n//2+1):
        print(point, end='')
        for j in range(i, n//2+1):
            print(len(point)*' ', end='')
        print(point, end='')
        print()
    if n % 2 == 1:
        print(point+point)

    for i in range(n//2, 0, -1):
        print(point, end='')
        for j in range(i, n//2+1):
            print(len(point)*' ', end='')
        print(point, end='')
        print()


def L(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (j == 0 or i == n-1):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def M(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (n % 2):
                if (j == 0 or j == n-1 or i == j and i <= n//2 or i+j == n-1 and i <= n//2):
                    print(point, end="")
                else:
                    print(len(point)*" ", end="")
            else:
                if (j == 0 or j == n-1 or i == j and i < n//2 or i+j == n-1 and i < n//2):
                    print(point, end="")
                else:
                    print(len(point)*" ", end="")
        print()


def N(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (j == 0 or j == n-1 or i == j):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def O(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or j == 0 or j == n-1 or i == n-1):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def P(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or j == 0 or j == n-1 and i <= n//2 or i == n//2):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def Q(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if ((i == 0 and (j != 0 and j != n-1)) or (i == n-2 and (j != 0 and j < n-2)) or (j == 0 and (i != 0 and i < n-2)) or (j == n - 1 and (i != 0 and i != n-2)) or ((n // 2 < i < n) and (j > n // 2) and (i == j))):
                print(point, end=" ")
            else:
                print(len(point)*" ", end=" ")
        print()


def R(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or j == 0 or j == n-1 and i <= n//2 or i == n//2 or i == j and i > n//2):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def S(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or j == 0 and i < n//2 or i == n//2 or i == n-1 or j == n-1 and i > n//2):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def T(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (not n % 2):
                if (i == 0 or j == n//2-1):
                    print(point, end="")
                else:
                    print(len(point)*" ", end="")
            else:
                if (i == 0 or j == n//2):
                    print(point, end="")
                else:
                    print(len(point)*" ", end="")
        print()


def U(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (j == 0 or j == n-1 or i == n-1):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def V(point: str, n: int) -> None:
    k = 0
    i = n - 1
    j = 1
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            print(len(point)*" ", end='')
        print(point, end='')
        for j in range(1, i * 2):
            print(len(point)*" ", end='')
        if (i >= 1):
            print(point, end='')
        print()


def W(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (j == 0 or j == n-1 or i == j and i >= n//2 or i+j == n-1 and i >= n//2):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def X(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == j or i+j == n-1):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()


def Y(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (n % 2):
                if (i == j and i <= n//2 or i+j == n-1 and i <= n//2 or i > n//2 and j == n//2):
                    print(point, end="")
                else:
                    print(len(point)*" ", end="")
            else:
                if (i == j and i < n//2 or i+j == n-1 and i < n//2 or i >= n//2 and j == n//2-1 or i >= n//2 and j == n//2):
                    print(point, end="")
                else:
                    print(len(point)*" ", end="")
        print()


def Z(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n-1 or i+j == n-1):
                print(point, end="")
            else:
                print(len(point)*" ", end="")
        print()

# A('* ', 9)

# print()
# A('* ', 6)

# B('* ', 9)

# print()
# B('* ', 6)

# C('* ', 9)

# print()
# C('* ', 6)

# D('* ', 9)

# print()
# D('* ', 6)

# E('* ', 9)

# print()
# E('* ', 6)

# F('* ', 9)

# print()
# F('* ', 6)

# G('* ', 9)

# print()
# G('* ', 6)

# H('* ', 9)

# print()
# H('* ', 6)

# I('* ', 9)

# print()
# I('* ', 6)

# J('* ', 9)

# print()
# J('* ', 6)

# K('* ', 9)

# print()
# K('* ', 6)

# L('* ', 9)

# print()
# L('* ', 6)

# M('* ', 9)

# print()
# M('* ', 6)

# N('* ', 9)

# print()
# N('* ', 6)

# O('* ', 9)

# print()
# O('* ', 6)

# P('* ', 9)

# print()
# P('* ', 6)

# Q('* ', 9)

# print()
# Q('* ', 6)

# R('* ', 9)

# print()
# R('* ', 6)

# S('* ', 9)

# print()
# S('* ', 6)

# T('* ', 9)

# print()
# T('* ', 6)

# U('* ', 9)

# print()
# U('* ', 6)

# V('* ', 9)

# print()
# V('* ', 6)

# W('* ', 9)

# print()
# W('* ', 6)

# X('* ', 9)

# print()
# X('* ', 6)

# Y('* ', 9)

# print()
# Y('* ', 6)

# Z('* ', 9)

# print()
# Z('* ', 6)

    # print(f'''
    # {chr(i+65)}('* ',9)\n
    # print()
    # {chr(i+65)}('* ',6)\n
    # ''')

