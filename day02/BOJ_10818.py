# 입력한 수의 최대 최소값 결과로 출력하기
#  print(max()),prin(min())

num = int(input())
nums = list(map(int,input().split()))       # 내가 못한 부분

print(min(nums),max(nums))

# ==ver2===
num = input()
numbers = list(map(int,input().split()))
print(min(numbers),max(numbers))