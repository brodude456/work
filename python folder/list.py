input1=input("enter become")
list=["i love you honey","bla blanews","somthing somemmit"]
print(list)
lis_for_list=[]
k=0
for x in list:
    du=0
    mu=4
    while True:
        lis_for_list=x[du:mu]
        if lis_for_list=="you " or lis_for_list=="news" or lis_for_list=="mmit":

            if lis_for_list=="mmit" or lis_for_list=="news" and input1[0]!=" ":
                input1=" "+ input1

            if input1[-1]==" ":
                y=x.replace(lis_for_list,input1)
                print(y)
                list[list.index(x)]=y
                break

            else:
                input1=input1+" "
                y=x.replace(lis_for_list,input1)
                print(y)
                list[list.index(x)]=y
                break

        du += 1
        mu += 1

print(list)


