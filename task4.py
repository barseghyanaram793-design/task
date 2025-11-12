n = int(input("enter number: "))
if n>0:
    print("Drakan")
elif n<0:
    print("Bacasakan")
else:
    print("ZEro")
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


a = int(input("enter number: "))
b = int(input("enter number: "))
c = int(input("enter number: "))

if a>b and a>c:
    print("Max A")
    if b>c:
        print("Min C")
    else:
        print("Min B")
elif b>a and b>c:
    print("Max B")
    if c>a:
        print("Min A")
    else:
        print("Min C")
elif c>a and c>b:
    print("Max C")
    if a>b:
        print("Min B")
    else:
        print("Min A")
else:
    print("a=b=c")



