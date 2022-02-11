n = int(input())        #정수로 입력받음
a = []

for i in range(1,n+1):      # 1~입력 정수까지
    square_num = i*i        #제곱수
    a.append(square_num)    #

print(a)


# 리스트 내포를 이용하기
a = [i*i for i in range(1,n+1)]
print(a)