def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
n=int(input("select the option 1,2,3,4"))
a=int(input("enter the first number"))
b=int(input("enter the second number"))
if n==1:
    print(a,"+",b,"=",add(a,b))
elif n==2:
    print(a,"-",b,"=",sub(a,b))
elif n==3:
    print(a,"*",b,"=",mul(a,b))
elif n==4:
    print(a,"/",b,"=",div(a,b))
else:
    print("please select above option")

