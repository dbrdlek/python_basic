# Function(함수) & Lambda(람다)

# 함수 정의 방법
# def 함수명(parameter):
# 	code 구현

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요
# 함수 선언 후에 사용가능

# Ex.1
def hello(world):
	print('Hello', world)

hello('python!')
hello(7777)

# Ex.2
def hello_return(world):
	val = 'Hello ' + str(world)
	return val

str_1 = hello_return('hihi')
print(str_1)

# Ex.3 (다중 리턴)
def func_mul(x):
	y1 = x * 100
	y2 = x * 200
	y3 = x * 300
	return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(type(val1),val1 , val2, val3)


# Ex.4 데이터 타입 반환 --> 리턴할 때 형식을 지정할 수 있음
def func_mul2(x):
	y1 = x * 100
	y2 = x * 200
	y3 = x * 300
	return (y1, y2, y3)  # 여기서 [] = 리스트 () = 튜플 {} = 딕셔너리 반환 가능

lt = func_mul2(100)
print(lt, type(lt))

# Ex.5
# *args  --> 가변이다.
# 다양한 매개변수 형태를 받아서 함수의 흐름을 바뀔때는 이렇게 된다
# 반환 타입은 튜플이다
def args_func(*args):
	print(args)
	# for t in args:
	# 	print(t)
	for i, v in enumerate(args):   # i = 인덱스, v = 값
		print(i, v)

args_func('kim')
args_func('kim', 'Park', 'Lee')

# *kwargs  키워드의 줄임말 
# 반환타입 -> *표가 하나면 튜플 **면 딕셔너리
def kwargs_func(**kwargs):
	print(kwargs)
	for k, v in kwargs.items():
		print(k, v)

kwargs_func(name1='kim')
kwargs_func(name1='kim', name2='park', name3 = 'Lee')

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
	print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim')
example_mul(10, 20, 'park', 'kim', age1 = 24, age2 = 35)

# 중첩함수(클로저)
# 데코레이터 클로저
def nested_func(num):
	def func_in_func(num):
		print('>>>>', num)
	print('in func')
	func_in_func(num + 10000)

nested_func(10000)


# Ex.6 (himt)
def func_mul3(x : int) -> list:
	y1 = x * 100
	y2 = x * 200
	y3 = x * 300
	return (y1, y2, y3)

print(func_mul3(5))

# lambda Ex.1
# 쓰는 이유 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화).. -> 메모리 초기화

# 일반적 함수
def mul_10(num : int) -> int:
	return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))
print(var_func(10))

# 람다식 함수 (lambda 매개변수들: 식)(인수들)
lambda_mul_10 = lambda num: num * 10
print('lambda :',lambda_mul_10(10))


def func_final(x, y, func):
	print(x * y * func(10))

func_final(10, 10, lambda_mul_10)
print(func_final(10, 10, lambda x : x * 1000))


