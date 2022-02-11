# # 영_숫자단어가 띄어쓰기 없이 주어진다.
# from dataclasses import replace
# # 딕셔너리와 문자열 메소드
# # 영단어를 숫자로 replace 한다. 
            
# solution(s)라는 함수 선언 (s ==입력 문자열)
def solution(s):
    # 영단어 딕셔너리
    en_num = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
         'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for i in en_num:
        # 딕셔너리에 있는 영단어의 인덱스 값으로 영단어를 replace 한다. 
        s = s.replace(i, str(en_num[i]))
        # s = s.replace(i,en_num.index(i))
   
    return int(s)

# ====

def solution(s):
    nswer = 0
    # 영단어 딕셔너리
    en_num = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']
    # en_num.key()라고 하지 않아도 for문에서는 자동으로 key값으로 반환한다.  
    for i in en_num:
        # 딕셔너리에 있는 영단어의 인덱스 값으로 영단어를 replace 한다. 
        s = s.replace(i, str(en_num.index(i)))
        
    answer = int(s)
    return answer