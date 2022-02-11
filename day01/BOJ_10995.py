#BOJ109995 번 별찍기 20
# 입력 ==  5
# ==출력==
# * * * * *
#  * * * * *
# * * * * *
#  * * * * *
# * * * * *
T = int(input())
for i in range(T):
    if i%2 ==0:
        print('* '*T)
    else:
        print(' *'*T)

 # print("* "*N if i%2 == 0 else " *"*N)