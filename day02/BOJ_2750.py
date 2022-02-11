# 첫째 줄에 수의 개수 
# N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 
# 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 
# # 수는 중복되지 않는다.

num =int(input())
result = [int(input()) for _ in range(num)]  #입력수를 하나의 리스트로 받는다. 
# nums = map(int,input().split())
 
print(sorted(result),seq='\n')


