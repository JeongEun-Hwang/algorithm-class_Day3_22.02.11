a = []

for _ in range(5):
    numbers = list(map(int,input().split()))
    a.append(numbers)

for i in range(5):
    for j in range(5):
         print(a[i][j],end="")
        # print()# 한줄로 띄어쓰기로 출력된다.
    print()# 줄 변경으로 출력되기 위해서
print(a)


# 정수 n을 입력받아, 1부터 n까지의 제곱수를 리스트로 만들어 출력하는 프로그램을 작성하라.

# 리스트 내포를 이용한다.

n = int(input())

