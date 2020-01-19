# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = "NiceMan"
str3 = ''
str4 = str('ace')

# 문자열 길이 구하기 len
print(len(str1), len(str2), len(str3), len(str4))

print('------------------------\n')

# escape 문자
escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab\t"
print(escape_str2)

print('------------------------\n')

# Raw String
# 이스케이프 문자가 적용되지 않음
# 문자열에 있는 그대로 표시 주로 경로를 표시할때 쓰임
raw_s1 = r'minu:\lib\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

print('------------------------\n')

# Multi line (멀티라인)  
# \ 기호가 없으면 에러 이 기호 뒤에서 문자열이 나온다고 인식
multi = \
"""
문자열

멀티라인

테스트
"""
print(multi)

print('------------------------\n')

# 문자열 연산
str_01 = "*"
str_02 = 'abc'
str_03 = 'def'
str_04 = "Niceman"

print(str_01 * 100)
print(str_02 + str_03)
# print(str_01 + 3 )  # 숫자를 더하기는 둘의 형이 달라서 사용할 수 없음
# in 연산자
# a라는 글자가 str_04에 포함되어 있는지 물어보는거
print('a' in str_04)  # a 가 있으니까 True 반환
print('f' in str_04)
print('z' not in str_04)

print('------------------------\n')

# 문자열 형 변환
print(str(77) + 'a')  # 숫자를 문자형으로 변환 문자로 인식해서 문자 +도 가능
print(str(10.4))

print('------------------------\n')

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
a = 'niceman'
b = 'orange'

print(a.islower())  # 전부 소문자인지 물어보는 함수 (반환 boolean)
print(b.endswith('s'))  # 끝 글자가 s로 끝나는지 물어보는 함수
print(a.capitalize())  # 첫 글자만 대문자로 바꾸기
print(a.replace('nice', 'good'))  # 처음 ''를 두번째 ''로 바꾸기
print(list(reversed(b)))  # list를 써야지 reversed()함수를 사용 할 수 있다 모든 문자 반대로

print('------------------------\n')

a = 'niceman'
b = 'orange'
# python은 문자열은 모두 인덱싱처럼 된다.
# 그래서 밑에처럼 사용하면 0번째 부터 3번째 글자가 나온다
print(a[0:3])
print(a[0:4])
print(a[0:len(a)])  # 0번째 부터 a라는 문자의 길이까지 라는 뜻
print(a[:])  # 처음부터 끝가지 나온다
print(b[0:4:2])  # 3번째 옵션만큼 쩜핑을 하면서 슬라이싱 한다
print(b[1:-2])  # 1번째 인덱스 부터 -2번째(역순) 나온다
print(b[::-1])  # 처음부터 끝까지 나오는데 역순으로 표시된다(리버스랑 비슷하다)


