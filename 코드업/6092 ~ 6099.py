# 6092
# n = int(input())      #개수를 입력받아 n에 정수로 저장
# a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

# for i in range(n) :  #0부터 n-1까지...
#   a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

# d = []                     #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
# for i in range(24) :  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
#   d.append(0)        #각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.

# for i in range(n) :    #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
#   d[a[i]] += 1

# for i in range(1, 24) :  #카운트한 값을 공백을 두고 출력
    # print(d[i], end=' ')

# 참고 
# - d = []              #어떤 데이터 목록(list) 을 순서대로 저장하기 위해 아무것도 없는 리스트 변수 만들기 
# - d.append(값)  #d 리스트의 마지막에 원하는 값을 추가(append)해 넣음  
# - d[a[i]] += 1     #2중 리스트 참조 : 만약 a[i]의 값이 1이었다면? d[1] += 1 이 실행되는 것이다. 1번 카운트 1개 증가.. 

# 어떤 값을 기록했다가 다시 사용할 필요가 있을 때, 필요한 변수(variable)를 만들어 사용하는 것처럼, 
# 여러 개의 값을 하나로 묶어 목록으로 기록했다가 다시 사용할 필요가 있을 때, 리스트(list)를 만들어 사용할 수 있다. 
# 리스트는 변수들을 모아 놓은 변수라고 생각할 수도 있고, 참조번호를 이용해 간단하고 편리하게 사용할 수 있다.

# 6093
# n = int(input())
# k = input().split()

# for i in range(n):
#     k[i]=int(k[i])

# for i in range(n-1, -1, -1):
#     print(k[i], end=' ')

# 6094
# n = int(input())
# k = input().split()

# for i in range(n):
#     k[i]=int(k[i])

# min = k[0]

# for i in range(n):
#     if min >= k[i]:
#         min = k[i]

# print(min)

# 6095
# d=[]    #대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기 
# for i in range(20):
#     d.append([])    #리스트 안에 다른 리스트 추가해 넣기 
#     for j in range(20):
#         d[i].append(0)  #리스트 안에 들어있는 리스트 안에 0 추가해 넣기 

# n = int(input())
# for i in range(n):
#     x,y = map(int, input().split())
#     d[x][y] = 1

# for i in range(20):
#     for j in range(20):
#         print(d[i][j], end=' ') #공백을 두고 한 줄로 출력 
#   print()

# ... 
# d=[]
# for i in range(20) : 
#   d.append([])
#   for j in range(20) :  
#     d[i].append(0)
# ...  

# 위와 같이, 모두 0이 채워진 2차원 리스트를 만드는 코드를 아래와 같은 방법으로 짧게 만들 수도 있다. 
# ... [0 for j in range(20)]  #20개의 0이 들어간 [0, 0, 0, ... , 0, 0, 0] 리스트 
# 아래처럼 작성하면 위와 같은 리스트가 20개가 들어간 리스트를 한 번에 만들어 준다. 

# d = [[0 for j in range(20)] for i in range(20)] 

# 이러한 리스트 생성 방식을 List Comprehensions 라고 한다. 

# 6096
# 19*19 크기, 범위 설정 오류가 있었다.
# d = []
# for i in range(19):
#     d.append([])
#     for j in range(19):
#         d[i].append(0)

# for i in range(19): 
#     d[i] = list(map(int, input().split()))


# n = int(input())

# for i in range(n):
#     x,y = map(int, input().split())

#     for j in range(19):
#         if d[j][y-1] == 0:
#             d[j][y-1] = 1
#         else:
#             d[j][y-1] = 0

#         if d[x-1][j] == 0:
#             d[x-1][j] = 1
#         else:
#             d[x-1][j] = 0

# for i in range(19) : 
#     for j in range(19) : 
#         print(d[i][j], end=' ') 
#     print()

# 6097
# k = []
# a,b = map(int, input().split())

# for i in range(a):
#     k.append([])
#     for j in range(b):
#         k[i].append(0)

# n = int(input())
 
# for i in range(n):
#     l,d,x,y = map(int,input().split())

#     if d == 0:
#         for j in range(l):
#             k[x-1][y-1+j]=1
    
#     else:
#         for j in range(l):
#             k[x-1+j][y-1]=1

# for i in range(a):
#     for j in range(b):
#         print(k[i][j], end = ' ')
#     print()

# 6098

d = []
for i in range(10):
    d.append([])
    for j in range(10):
        d[i].append(0)

for i in range(10):
    d[i] = list(map(int, input().split()))

x, y = 1, 1

while True:
    if d[x][y] == 0:
        d[x][y] = 9
    elif d[x][y] == 2:
        d[x][y] = 9
        break

    if d[x+1][y] == 1 and d[x][y+1] == 1:
        break

    if d[x][y+1] != 1:
        y = y+1
    elif d[x+1][y] != 1:
        x = x+1

for i in range(10):
    for j in range(10):
        print(d[i][j], end = ' ')
    print()

        


