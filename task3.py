# Arajadranq 3
print("xndir1")
a = int(input("Enter number: "))
if a>0:
    print("Drakan")
else:
    ("Bacasakan kam 0")

print("xndir2")
a = int(input("Enter number: "))
if a % 2 == 0:
    print("Zuyg tiv")
else:
    print("Kent")
#?

print("xndir3")
a = int(input("Enter number: "))
b = int(input("Enter number: "))
if a > b:
    print("a tiv met e")
elif b>a:
    print("b tiv met e")
else:
    print("a=b")

print("xndir4")
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
if a > b and a > c:
    print("a tiv met e")
elif b >a and b > c:
    print("b tiv met e")
elif c > a and c > b:
    print("c tiv met e")
else:
    print("bolor tvere havasar en")

print("xndir5")
a = int(input("Enter number:"))
if a > 0:
    print("a tiv Drakan e")
elif a < 0:
    print("a tiv Bacasakan e")
else:
    print("a = 0")

print("xndir6")
gnahatakan = int(input("Enter gnahatakan: "))
if 90 <= gnahatakan <= 100:
    print("Excellent")
elif 70 <= gnahatakan <= 89:
    print("Good")
elif 50 <= gnahatakan <= 69:
    print("Average")
elif 0 <= gnahatakan <= 49:
    print("Fail")
else:
    print("invalid input")

print("xndir7")
gin = int(input("Enter gin"))
if 10000 <= gin <= 50000:
    print("Zexch 10%")
elif gin >= 50000:
    print("Zexch 30%")
elif gin < 0:
    print("Invalid input")
else:
    print("Zexch 0%")

print("xndir8")
age = int(input("Enter tariq"))
passport = input("Enter yes or no")
if age <= 0:
    print("Invalid input")
elif age >= 18:
    if passport == "yes":
        print("Karox e qvearkel")
    elif passport == "no":
        print("Chi karox qvearkel")
    else:
        print("Invalid input")
else:
    print("ir tariqy 0-18, chi karox qvearkel")

print("xndir9")
gnahatakan = int(input("Enter gnahatakan: "))
if  gnahatakan < 0 or gnahatakan > 100:
    print("Invalid input")
else:
    ararka = input("Enter math or english")

    if gnahatakan >= 50:
        if ararka == "math":
            print("Ancel e math")
        elif ararka == "english":
            print("Ancel e english")
        else:
            print("Chi ancel")
#?

print("xndir10")
a = int(input("Enter number: "))
print("Drakan") if a > 0  else  print("bacasakan")

print("xndir11")
a = int(input("Enter number: "))
b = int(input("Enter number: "))
print("Met e a ") if a > b  else  print ("Met e b")

print("xndir12")
gin = int(input("Enter gin: "))
print("Zexch ka") if gin > 10000 else print("Zexch cka")

print("xndir13")
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
if a > b:
    if a > c:
        print("a amenametn e")
    else:
        print("a < c")
else:
    print("a poqr kam havasar e b")

print("xndir14")
t = int(input("Enter t°: "))
if t < 0:
    print("Sarn e")
elif 0 <= t <= 30:
    print("Haeli e")
else:
    print("Taq e")

print("xndir15")
month = int(input("Enter month: "))

if month == 1 or month == 2 or month==12:
    print("Dzmer")
elif month==3 or month==4 or month==5:
    print("Garun")
elif month==6 or month==7 or month==8:
    print("Amar")
elif month == 9 or month == 10 or month == 11:
    print("Ashun")
else:
    print("invalid input")



print("xndir16")
a = int(input("Enter number: "))
print(a * 4) if a > 0  else  print("a")

print("xndir17")
account = input("Enter account(savings or current ): ")
amount = int(input("Enter amount: "))
if account == "savings":
    if amount > 100000:
       print("High balance")
    elif amount>0:
        print("Normal balanse")
    else:
        print("invalid")
elif account == "current":
    print("Business balanse")
else:
    print("Anhayt balanse")

print("xndir18")
exam = int(input("Enter miavore: "))
assignment = int(input("Enter miavore: "))
if exam >= 50 and assignment >= 50:
    print("Ancel e")
elif exam >= 50 or assignment >= 50:
    print("paymanakan e ancel")
elif exam >=0 and assignment >= 0:
    print("Chi ancel")
else:
    print("invalid input")

print("xndir19")
a = int(input("Enter amboxj tiv: "))
if a > 0:
    if a % 2 == 0:
        print("Drakan ev zuyg")
    else:
        print("Drakan, bayc kent e")
else:
    print("Drakan che")