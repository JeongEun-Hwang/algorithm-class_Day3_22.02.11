# from itertools import count
# name = input().split()

# # 빈 딕셔너리 만들기
# count_name ={}
# # 딕셔너리에 선수이름을 넣고, 그수를 value값으로 지정하기
# # count_name[name] = name.count(name)
# for i in name:
#     count_name[i] = name.count(i)

# #  가장 이름이 적은 선수 카운트
# min_name = min(count_name.values())

# # 선수 이름과 카운트 줄력하기
# for  key,val in count_name.items():
#         if val == min_name:
#             # print(key,val)
#             print(key)
      
# print(val)
# # ====

from unittest.util import _MIN_COMMON_LEN


players = input().split()

# 빈 딕셔너리 만들기
foul ={}

for name in players :
    # 이미 파울을 했니?
    if name in foul:
        foul[name] += 1
    # 파울을 한번도 안했니?
        foul[name] =1

# 파울을 가장 적게한 선수 뽑기
min_foul = min(foul.values())

for player,foul in foul.items():
    if foul == min_foul:
        print(player)
print(min_foul)