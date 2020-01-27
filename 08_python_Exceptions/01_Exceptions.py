# 파이썬 예외처리 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세서에서 발생하는 예외 처리 중요
# linter : 코드 스타일, 문법 체크

#### SyntaxError : 잘못된 문법
# print('test)
# if True
# 	pass
# x => y


#### NameError : 참조변수 없음
a = 10
b = 15
# print(c)


#### ZeroDivisionError : 0 나누기 에러
# print(10 / 0)


#### IndexError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3]) # 예외 발생


#### KeyError
dic = {'name': 'kim', 'Age': 33, 'City': 'seoul'}

# print(dic['hobby'])  # KeyError
print(dic.get('hobby')) # 그래서 이걸 사용해야 됨


#### AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 나오는 에러
import time
print(time.time())
# print(time.month())


#### valuError : 참조 값이 없을 때 발생
x = [1, 5, 9]

# x.remove(10)
# x.index(10)


#### FileNotFoundError
# f = open('test.txt', 'r') # 예외 발생


#### TypeError
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y)
# print(x + z)

# print(x + list(y))  # list로 형변화 후 결합 하는거


# 항상 예외가 발생하지 않은 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)


# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명 1
# except : 에러명 2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# Ex. 1
name = ['Kim', 'Lee', 'Park']

try:
	z = 'Kim' # Cho라고 하면 예외 발생
	x = name.index(z)
	print('{} Found it! {} in name'.format(z, x+1))
except ValueError:
# except: # 어떤 에러가 발생할지 모르면 이렇게 해줘도 된다 모든 에러에 대해 캐치한다
	print('Not Found it! - Occurred ValueError!')
else:
	print('Ok! else!')  # Error가 발생하지 않았을 경우에만 실행 (Try 구문 통과 후 실행)
finally:
	print('finally ok!')

print()


# Ex. 2
try:
	z = 'Park' # Cho라고 하면 예외 발생
	x = name.index(z)
	print('{} Found it! {} in name'.format(z, x+1))
except: # 모든 에러를 처리(Exception)
	print('Not Found it! - Occurred Error!')
else:
	print('Ok! else!')  # Error가 발생하지 않았을 경우에만 실행 (Try 구문 통과 후 실행)
finally:
	print('finally ok!')

print()

# 예제3
try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:
    print(e)  # 에러 내용 출력
    # pass # 임시로 에러 해결 시 예외 처리
else:
    print('ok! else!')
finally:
    print('ok! finally!')  # 무조건 수행 됨

print()

# Ex. 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
	print('Try')
finally:
	print('Ok Finally!!!!')


# Ex. 5
name = ['Kim', 'Lee', 'Park']

try:
	z = 'Kim' # Cho라고 하면 예외 발생
	x = name.index(z)
	print('{} Found it! {} in name'.format(z, x+1))
except ValueError as l:
	print(l)
	print('Not Found it! - Occurred ValueError!')
except IndexError:
	print('Not Found it! - Occurred IndexError!')
except Exception:
	print('Not Found it! - Occurred Error!')
else:
	print('Ok! else!')  # Error가 발생하지 않았을 경우에만 실행 (Try 구문 통과 후 실행)
finally:
	print('finally ok!')

print()


# Ex. 6
# 예외 발생 : raise 
# raise 키워드로 예외 직접 발생
try:
	# a = '333'
	a = 'Kim'
	if a == 'Kim':
		print('Ok 허가!')
	else:
		raise ValueError
except ValueError:
	print('문제 발생!')
except Exception as f:
	print(f)
else:
	print('Ok')


