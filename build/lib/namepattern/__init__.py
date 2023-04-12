def A(point: str, n: int) -> None:
    for i in range(n):
        for j in range(n):
            if (i == 0 and j!=0 and j!=n-1 or j == 0 and i!=0 or j == n-1 and i!=0 or i == n//2):
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
            if (i == 0 and j!=0 or j == 0 and i!=0 and i!= n-1 or i == n-1 and j!=0 and j < n//2 or j == n//2 and i >= n//2 or i == n//2 and j > n//2 or j == n-1 and i > n//2):
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
            if (i == 0 and j!=n-1 or j == 0 or j == n-1  and i < n//2 and i!=0  or i == n//2 and j!=n-1 or i == j and i > n//2):
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



class Namepattern:
    def __init__(self,pattern: str,design:str="^^",n:int=5) -> None:
        self.pattern=pattern
        self.design=design
        self.n=n

    def displayName(self) -> None:
            '''This function will print the any name as pattern'''
            # create a docstring
            pattern=self.pattern.upper()
            design=self.design
            n=self.n
            for i in pattern:
                if i == "A":
                    A(design, n)
                elif i == "B":
                    B(design, n)
                elif i == "C":
                    C(design, n)
                elif i == "D":
                    D(design, n)
                elif i == "E":
                    E(design, n)
                elif i == "F":
                    F(design, n)
                elif i == "G":
                    G(design, n)
                elif i == "H":
                    H(design, n)
                elif i == "I":
                    I(design, n)
                elif i == "J":
                    J(design, n)
                elif i == "K":
                    K(design, n)
                elif i == "L":
                    L(design, n)
                elif i == "M":
                    M(design, n)
                elif i == "N":
                    N(design, n)
                elif i == "O":
                    O(design, n)
                elif i == "P":
                    P(design, n)
                elif i == "Q":
                    Q(design, n)
                elif i == "R":
                    R(design, n)
                elif i == "S":
                    S(design, n)
                elif i == "T":
                    T(design, n)
                elif i == "U":
                    U(design, n)
                elif i == "V":
                    V(design, n)
                elif i == "W":
                    W(design, n)
                elif i == "X":
                    X(design, n)
                elif i == "Y":
                    Y(design, n)
                elif i == "Z":
                    Z(design, n)
                elif i==" ":
                    print("\n")
                else:
                    print("Invalid character found at index", i, ". Program Terminated.")
                    exit(0)
                #space between letters
                print("\n")

# displayName("Arij32it ghosh")