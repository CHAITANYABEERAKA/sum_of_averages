c = int(input("enter length of the list : "))
a = list(map(int,input("enter the elements : ").strip().split()))[:c]
b = []
def sublist(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]

#for i in range(0,c):
#    elements = int(input("enter elements : "))
#    a.append(elements)
n = int(input("enter number of parts : "))
x = list(sublist(a,n))
print(x)
for i in x:
    print(i)
    z = sum(i)/len(i)
    b.append(z)
    print("average = ",z)
print("sum of average  = ",sum(b))


    
    

