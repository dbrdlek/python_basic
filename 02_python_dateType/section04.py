# Python 데이터 타입 종류
'''
  Boolean  --> 1: Ture 0: False
  Numbers  --> 정수 실수
  String   --> 문자
  Bytes
  이 밑에부터 집합 자료형
  Lists         
  Tuples
  Sets
  Dictionaries

  + : 더하기
  - : 빼기
  / : 나누기
  // : 나웠을때 몫
  % : 나눴을때 나머지
  ** : 지수(제곱)
  단항 연산자
'''

# 데이터 타입
# 문자형
v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
	"name" : "Kim",
	"age" : 25
}
v_list = [3, 5, 7]  # 배열
v_tuple = 3, 5, 7
v_set = {7, 8 ,9}

# 괄호 안에 있는 게 어떤 타입인지 알려주는거
print(type(v_tuple))
print(type(v_set))
print(type(v_float))

print('-----------------------------\n')

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999999
big_int2 = 7777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5   # 0.5를 의미
f4 = 10.  # 10.0을 의미

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)  # f1을 f2 만큼 제곱
print(f3 + i2)   # 실수와 관련된 연산은 실수로 자동 형변환

result = f3 + i2
print(result, type(result))

print('-----------------------------\n')

a = 5.
b = 4
c = 10

print( type(a), type(b) )
result2 = a+b
print(result2)

# 형 변환
# int, float, complex(복소수)
print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

print('-----------------------------\n')

y = 100
y += 100
print(y)


# 수치 연산 함수
# 참조 python math 함수 http://docs.python.org/3/library/math.html

print('-----------------------------\n')

print(abs(-7))  # 절댓값 구하기
n, m = divmod(100, 8) # divmod라는 함수는 100을 8로 나웠을때 몫을 처음 나머지를 뒤에 담긴다
print(n, m)

import math

print(math.ceil(5.1))  # 올림
print(math.floor(3.874)) # 내림







