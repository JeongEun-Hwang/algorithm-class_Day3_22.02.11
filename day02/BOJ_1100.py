# 하얀칸_하얀칸 위에 말이 몇개 있는지 출력
# 체스판 행렬 범위= 8*8
# 하얀 칸은 행과 열의 위치
#  [0,0] [0,2] [0,4] [0,6] [1,1], [1,3]
#  행,렬을 더했을 때 '짝'이면 하얀칸
# .append()로 리스트에 입력값을 넣을 경우, 
# input()해야 리스트로 접근할 수 있다. 
chess = []
h_count=0       #체스말 카운트

for _ in range(8):      #체스판(8*8)에 체스말(./F) 입력
        chess.append(input())

for l in range(8):      #체스판 행과 열의 하얀칸에 말이 몇개 있는지 count
    for r in range(8):
        if (r+l)%2 ==0  and chess[r][l]=='F':
            h_count +=1

print(h_count)


