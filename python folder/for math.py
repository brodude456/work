a=int(input("enter a numero"))
b=int(input("enter a second numero"))

counter=1

A=a
B=b

while True:

    A=A+1
    B=B+1

    if A/B==2 or A-B==B:

           print(A-a,",",A,B)

           break

    else:

           continue
