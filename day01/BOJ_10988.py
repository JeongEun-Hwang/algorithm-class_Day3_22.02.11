# 팰린드롬인지 확인하기
# 앞 == 거꾸로
palindrome =input()

if palindrome ==palindrome[::-1]:
    print('1')
else:
    print('0')

# print('1' if palindrome == palindrome[::-1] else)