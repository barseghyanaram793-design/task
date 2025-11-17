# Xndir1
n = int(input("Enter a number: "))
sum = 0
for i in range(n+1):
    sum += i
print(sum)

#Xndir2
for i in range(1,101):
    if i % 2 !=0:
        print(i)


#xndir3
n = int(input("Enter a number: "))
count = 0

while n>0:
    count +=1
    n = int(input("Enter a number: "))

print(count)


#xndir4
n = int(input("Enter a count: "))
sum = 0

for i in range(1, n + 1):
    a = int(input("Enter a number: "))
    sum += a
print(sum/n)


#xndir5
for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        print(result, end="\t")
    print()


#xndir6
n = int(input("Enter a count: "))
sum = 0

for i in range(n):
    a = int(input("Enter a number: "))
    if a % 2 != 0:
        continue
    sum+=a
print(sum)

#xndir7
n = int(input("Enter a count: "))

zuyg_qanak = 0
kent_qanak = 0
drakan_qanak = 0
bacasakan_qanak = 0
zero_qanak = 0
for i in range(n):
    a = int(input("Enter a number: "))
    if a % 2 == 0:
        zuyg_qanak += 1
    else:
        kent_qanak += 1
    if a>0:
        drakan_qanak += 1
    elif a<0:
        bacasakan_qanak += 1
    else:
        zero_qanak +=1
print(f"Zuygeri qanaky {zuyg_qanak} hat e")
print(f"Kent tvery {kent_qanak} hat e")
print(f"Drakan tver {drakan_qanak} hat e")
print(f"Bacas tver {bacasakan_qanak} hat e")
print(f"Zero tver {zero_qanak} hat e")


#xndir8

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += i**2
print(sum)

#xndir9

secret = 25
n=int(input("Enter a number: "))

while n != secret:
    print("Ches gushakel, noric nermucir")
    n = int(input("Enter a number: "))

print("Du haxtecir")

#xndir10

n=int(input("Enter a number: "))

sum1=0
while n!=0:
    sum1+=n
    n=int(input("Enter a number: "))


print(sum1)

#xdnir14

text1 = input("Enter a text: ")

text2 = ""

for i in text1:
    if not i.isdigit():
        text2 += i
print(text2)

#xndir15
n = int(input("Enter a number: "))

for i in range(1, n+1):
    if i % 2 == 0 and i % 3 == 0 and i % 5 != 0:
        print(i)

#xndir17
n = int(input("Enter a count: "))

even_sum = 0
odd_sum = 0

for i in range(1,n+1):
    a = int(input("Enter a number: "))
    if a % 2 == 0:
        even_sum += a
    else:
        odd_sum += a
print(even_sum)
print(odd_sum)


#xndir18

n = int(input("Enter a range: "))
sum = 0
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 !=0:
        sum += i

print(sum)

#xndir19

n = int(input("Enter a count: "))
sum = 0

for i in range(1,n+1):
    sum += i ** 2

print(sum/n)

# xndir21

text = input("Enter a text: ")
dzaynavorner = "aeiouAEIOU"
count = 0
for x in text:
    if x.isalpha() and x not in dzaynavorner:
        count += 1
print(count)

#xndir23
text1 = input("Enter a text: ")

text2 = ''
for i in text1:
    text2 = i + text2
print(text2)

#xndir24
for i in range(1,101):
    if i % 4 ==0 and i % 6 == 0:
        print(i)
        break

'''#xndir25
#tarberak1
i = int(input("Enter a number: "))
sum = 0
while i<0:
    sum+=i
    i = int(input("Enter a number: "))

#tarberak2

s = 0
while True:
    x = int(input("Enter a number: "))
    if x <0:
        break
    s+=x
print(s)'''

#xndir27

text = input("Enter a string: ")
count = 1
for tar in text:
    if tar == " ":
        count += 1
print(count)

#xndir28

n = int(input("enter a number: "))
count = 0
for i in range(1,n+1):
    if i % 3 ==0 or i % 7==0:
        count += 1

print(count)

#xndir29
text = input("Enter a text: ")
has_digit = False

for simvol in text:
    if simvol.isdigit():
        has_digit = True
        break
print(has_digit)

#xndir 30

n = int(input("Enter a range: "))
for i in range(1,n+1):
    if i % 3 ==0 and i % 5 == 0:
        continue
    print(i)


# #xndir31

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a>b:
    print("a is max")
elif b>a:
    print("b is max")
else:
    print("a=b")

# #xndir34
numbers = [12,43,54,56,55,35,23,55,67,65,1,4,2234,766,455]

for number in numbers:
    if 10 <= number <= 99 and number % 10 == 5:
        print(number)


#xndir35
sum = 0

while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    sum += number

print(sum)

#xndir36
count = 0

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    count += 1

print(count)

#xndir37
secret = 7

while True:
    tiv = int(input("Gushakir tivy: "))
    if tiv == secret:
        print("Gushakel es")
        break

    print("Pordzir krkin")

#xndir 38
sum = 0
count = 0

while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    sum += number
    count += 1

print(sum/count)

#xndir 41

max_number = None

while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    if max_number is None or number > max_number:
        max_number = number


print(max_number)
