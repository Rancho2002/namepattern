#K
n=int(input())
point=5
for i in range(n):
        for j in range(n):
            if(n%2): #odd
                if(j==0 or i>=n//2 and i-j==1 or i<=n//2 and i+j==n-2):
                    print(point,end="")
                # elif(n>5 and j<n//2-1):
                #     print(point,end="")
                else:
                    print(len(point)*" ",end="")
            else:
                if(j==0 or i>=n//2 and i==j or i+j==n-1 and i<n//2 or j<n//2 and i==n//2 or j<n//2 and i==n//2-1):
                    print(point,end="")
                else:
                    print(len(point)*" ",end="")
        print()

        