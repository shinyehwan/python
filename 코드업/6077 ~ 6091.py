# 6077
# n = int(input())
# s = 0
# for i in range(n+1):
#     if i%2 == 0:
#         s = s + i
# print(s)

# 6078
# while True:
#     n = input()
#     print(n)
#     if n == 'q':
#         break

# 6079
# a = int(input())
# sum = 0

# for i in range(50):
#     sum += i
#     if a<=sum:
#         print(i)
#         break
    
# n = int(input())
# s = 0
# c = 0
# while s<n:
#     c += 1
#     s = s+c
# print(c)

# 6080
# a,b = map(int, input().split())

# for i in range(1, a+1):
#     for j in range(1, b+1):
#         print(i, j)

# 6081
# n = int(input(), 16)
# for i in range(1,16):
#      print('%X*%X=%X' %(n, i, i*n), sep='') 

# 6082
# n = int(input())
# for i in range(1, n+1):
#     if i%10==3 or i%10==6 or i%10==9:
#        print('X', end=' ')
#     else:
#         print(i, end=' ')

# 6083
# r,g,b = map(int, input().split())
# count = 0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)
#             count+=1
            
# print(count)

# 6084
# h, b, c, s = map(int, input().split())
# print( round(h*b*c*s/8/1024/1024, 1), 'MB')

# total = h*b*c*s/8/1024/1024
# print("%0.1f MB" %total)


# 6085
# h, b, c = map(int, input().split())
# print( round(h*b*c/8/1024/1024, 2), 'MB')

# total = h*b*c*s/8/1024/1024
# print("%0.2f MB" %total)

# 6086
# a = int(input())
# s = 0
# c = 0
# while True:
#    s += c
#    c +=1
#    if s>=a:
#        break
# print(s)

# 6087
# n = int(input())
# for i in range(1, n+1):
#     if i%3==0:
#         continue
#     print(i, end=' ')

# 깃허브 푸쉬하는 과정에서 오류가 났음 깃허브에 있는 리포지토리가 로컬에서 사라져서 그런다.
# 문제해결하는데 시간이 좀 걸림, 강제로 푸쉬함

# 6088
# a,d,n = map(int, input().split())

# for i in range(2,n+1):
#     a+=d
# print(a)

# 6089
# a,r,n = map(int, input().split())

# for i in range(2,n+1):
#     a*=r
# print(a)

# 6090
# a,m,d,n = map(int, input().split())

# for i in range(2,n+1):
#     a = a*m+d

# print(a)

# 6091
a,b,c = map(int, input().split())
d = 1

while True:
    d+=1
    if d%a == 0 and d%b == 0 and d%c == 0:
        print(d)
        break
        
    