#first we will take inputs for numbers of testcases
t=int(input())

#loop t times
for _ in range(t):
    #taking input as a string and spliting it using '+' sign
    a,b=input().split('+')
    print(int(a)+int(b))
    