# # 크로아티아알파벳
# # 크로아티아 알파벳은 몇개?/ 목록에 없는 글자는 한글자씩 센다. 
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in croatia :
#     # if i in word:
#     # 공백으로 replace 하면 특정 케이스에서 길이를 제대로 인식하지 못하기 때문에 특성문자로 변환.
#     word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(word))



def get_total(n):
    return(n*(n+1))//2

result = get_total(100000000)
print(result)