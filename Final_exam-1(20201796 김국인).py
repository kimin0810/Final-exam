#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201796 이름 : 김국인

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    if target in my_string: #if문을 사용하여 target이 my_string에 들어 있는지 확인하고
        return 1 # 맞을 때는 return 값으로 1을 
    else: #아니라면 return 값을 0으로 한다.
        return 0
    
myString = "hello my name is korean" # 영소문자의 문장을 입력해 보았다.

Target = "name" # 부분 문자열이다.

a = solution(myString,Target) #a에 return 값을 저장한다.

print("결과:",a) #출력하면 결과 :1 이 나온다.





# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}

    texts = letter.split(' ') #모스부호가 들어있는 letter의 문자열을 ' ' 기준으로 끊어서 texts라는 리스트를 만든다.
    test = "" #변환된 영문자를 저장할 변수를 선언한다.
    for text in texts: #for문은 통해 texts에 저장된 리스트를 text에 순서대로 넣어서 작동한다.
        test += morse[text] #test 변수에 morse딕셔너리에 있는 변환문자를 이어서 넣는다.
    return test #test에 변환된 영문자를 반환한다.
   
message = ".. .-.. --- ...- . -.-- --- ..-" #iloveyou를 모스부호로
a = solution(message)
print(a)





# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    number = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    #숫자 0부터 9까지를 각각 알파벳과 대응하게 딕셔너리를 설정해줌
    age_str = str(age)
    #숫자 나이를 문자열로 변환시키고 저장
    age_number = list(age_str)

    #문자열로 변환한 숫자를 list로 각각 나누어서 저장한다
    result = ''
    #변환한 알파벳을 저장할 변수를 설정해 준다.

    for char in age_number: #문자열로 변환된 숫자를 차례대로 char변수에 적용
        result += number[char] #number딕셔너리에 char가 key로 적용되고 값을 result에 저장
    return result    #변환된 나이를 리턴.

age = 52 #설정한 나이
a = solution(age)
print(a)






# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.

# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 
# return하도록 solution 함수를 완성해주세요.

# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    count = 0 #좌표의 개수를 카운트할 변수 선언

    # x좌표와 y좌표를 각각 -r2에서 r2까지 for문을 돌린다.
    for x in range(-r2, r2 + 1):
        for y in range(-r2, r2 + 1):

            #좌표의 거리는 x**2 + y**2 = z**2을 이용해서 비교 해본다.
            lengh = x**2 + y**2

            #원점에서 좌표까지의 거리가 r2보다 작고 r1보다 큰지 확인하고 count를 1증가시킨다.
            if r1**2 <= lengh <= r2**2:
                count += 1
    #총 count한 수를 반환한다.
    return count
r1 = 1 #임시로 값을 설정
r2 = 3
a = solution(r1, r2)
print(a)







# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항ss
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    num = list(map(str,numbers)) #매개변수의 숫자들을 문자열 리스트로 저장한다.

    #원소 크기가 1000이하이기 때문에 저장된 숫자를 3자리 이상의 수로 만들어서 ascii값으로 내림차순 정렬한다.
    number_sort = sorted(num, key = lambda x: x*3, reverse = True)
    
    #정리된 리스트를 join함수로 붙여서 result에 저장한다.
    result = ''.join(number_sort)

    #결과로 000처럼 0이 여러개 나올 수 있기 때문에 int형으로 바꾼 다음 다신 문자열로 바꿔 리턴한다.
    return str(int(result))

numbers = [8, 30, 17, 2, 23] #예시

a = solution(numbers)

print(a)