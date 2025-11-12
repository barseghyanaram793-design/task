# # Xndir1
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(n+1):
#     sum += i
# print(sum)
#
# #Xndir2
# for i in range(1,101):
#     if i % 2 !=0:
#         print(i)
#
#
# #xndir3
# n = int(input("Enter a number: "))
# count = 0
#
# while n>0:
#     count +=1
#     n = int(input("Enter a number: "))
#
# print(count)
#
#
# #xndir4
# n = int(input("Enter a count: "))
# sum = 0
#
# for i in range(1, n + 1):
#     a = int(input("Enter a number: "))
#     sum += a
# print(sum/n)
#
#
# #xndir5
# for i in range(1, 11):
#     for j in range(1, 11):
#         result = i * j
#         print(result, end="\t")
#     print()


# #xndir6
# n = int(input("Enter a count: "))
# sum = 0
#
# for i in range(n):
#     a = int(input("Enter a number: "))
#     if a % 2 != 0:
#         continue
#     sum+=a
# print(sum)

# #xndir7
# n = int(input("Enter a count: "))
#
# zuyg_qanak = 0
# kent_qanak = 0
# drakan_qanak = 0
# bacasakan_qanak = 0
# zero_qanak = 0
# for i in range(n):
#     a = int(input("Enter a number: "))
#     if a % 2 == 0:
#         zuyg_qanak += 1
#     else:
#         kent_qanak += 1
#     if a>0:
#         drakan_qanak += 1
#     elif a<0:
#         bacasakan_qanak += 1
#     else:
#         zero_qanak +=1
# print(f"Zuygeri qanaky {zuyg_qanak} hat e")
# print(f"Kent tvery {kent_qanak} hat e")
# print(f"Drakan tver {drakan_qanak} hat e")
# print(f"Bacas tver {bacasakan_qanak} hat e")
# print(f"Zero tver {zero_qanak} hat e")


# #xndir8

# n = int(input("Enter a number: "))
# sum = 0
#
# for i in range(1, n + 1):
#     sum += i**2
# print(sum)

# #xndir9
#
# secret = 25
# n=int(input("Enter a number: "))
#
# while n != secret:
#     print("Ches gushakel, noric nermucir")
#     n = int(input("Enter a number: "))
#
# print("Du haxtecir")

# #xndir10

n=int(input("Enter a number: "))
sum = 0

while n!=0:
    sum+=n
    n=int(input("Enter a number: "))


print(sum)