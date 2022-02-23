# 6025

# a, b = input().split()
# c = int(a) + int(b)
# print(c)

# 6026

# a, b = input().split()
# c = float(a) + float(b)
# print(c)

# 6027

# a = input()
# n = int(a)
# print('%x' %n)

# 6028

# a = input()
# n = int(a)
# print('%X' %n)

# 6029

# a = input()
# n = int(a, 16)
# print('%o' %n)

#6030

# n = ord(input())
# print(n)

# 6031

# c = int(input())
# print(chr(c))

# 6032

# c = int(input())
# print(-c)

# 6033
# n = ord(input())
# print(chr(n+1))

# 6034
# a, b= input().split()
# c = int(a) - int(b)
# print(c)

# 6035
# a, b = input().split()
# c = float(a) * float(b)
# print(c)

# 6036
# w, n  = input().split()
# print(w*int(n))

# 6037
# n = int(input())
# s = input()
# print(n*s)

# 6038
# a, b = input().split()
# print(int(a)**int(b))

# 6039
# f1, f2 = input().split()
# print(float(f1)**float(f2))

# 6040
# a, b = input().split()
# print(int(a)//int(b))

# 6041
# a, b = input().split()
# print(int(a)%int(b))

# 6042
# a = float(input())
# print(format(a,".2f"))


# 6043
# f1,f2 = input().split()
# f3 = float(f1)/float(f2)
# print(format(f3, ".3f"))

# 6044
# a,b = map(int, input().split())
# print(format(a + b, ".2f"))
# print(format(a - b, ".2f"))
# print(format(a * b, ".2f"))
# print(format(a // b, ".2f"))
# print(format(a % b, ".2f"))
# print(format(a / b, ".2f"))


# 6045
# a, b, c = map(int, input().split())
# sum = a+b+c
# avg = sum/3
# print(sum, format(avg, ".2f"))

# 6046
# a = int(input())
# print(2*a)
# print(a<<1)

# 6047
# a, b = map(int, input().split())
# print(a << b)

# 6048
# a, b = map(int, input().split())
# print(a<b)

# 6049
# a, b = map(int, input().split())
# print(a==b)

# 6050
# a, b = map(int, input().split())
# print(b>=a)

# 6051
# a, b = map(int, input().split())
# print(a!=b)

# 6052
# n = int(input())
# print(bool(n))

# 6053
# n = int(input())
# print(not bool(n))
# n = bool(int(input()))
# print(not n)

# 6054
# a, b = map(int, input().split())
# print(bool(a) and bool(b))

# 6055
# a, b = map(int, input().split())
# print(bool(a) or bool(b))

# 6056
# a, b = map(int, input().split())
# print(bool(a) != bool(b))

# c = bool(a)
# d = bool(b)
# print((c and not(d)) or (not(c) and not(d)))

# 6057
# a, b = map(int, input().split())
# print(bool(a) == bool(b))

# c = bool(a)
# d = bool(d)
# print((not c and not d) or (c and d))

# 6058
a, b = map(int, input().split())
c = bool(a)
d = bool(b)
print(not c and not d)
