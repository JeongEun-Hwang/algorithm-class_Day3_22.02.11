# 별 오른쪽 정렬
T = int(input())

for i in range (1,T+1): 
    print(('*'*i).rjust(5))

# for i in range(T):
#     # 공백 구하는 식 = n-i-1
#     # print(공백+별표)
#     print( (' '*(T-i-1)) + ('*'*(i+1)) )