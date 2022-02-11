# 오타맨 고창영_잘못된 단어 입력 횟수
T=int(input())

for i in range(T):
    n,word=(input().split())
    n = int(n)
    print(word[:n]+word[n:])