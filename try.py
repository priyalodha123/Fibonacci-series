#fibonacci series
n=int(input("enter the number till which u want to calculate fibonacci"))
a=0
b=1
print(a,b,end=" ")
for i in range(0,n-2):#range till n-2
    temp=a
    a=b
    b=temp+a
    print(b,end=" ")#printing the output
