# # 숫자합
# # 공백 없이 쓰여있다. split()==x
# # 입력으로 주어진 숫자 N개의 합을 출력
# # == int(input())
# # += input()


# # ==ver1===
# num = int(input())
# nums = int(input())

# print(sum(range(1,num+1)))

# # ver2=============
# num = int(input())
# nums = int(input())

# total = 0

# for i in range(1,num+1):
#     total +=i
# print(total)

# # 문자 = map한다. 

# num =input()

# total = sum(list(map(int,input())))
# print(total)
print(sum(list(map(int,input().split()))))
