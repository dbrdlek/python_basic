# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

import this # Python에 관한 설명 글이 나옴
import sys

# 파이썬 2.x vs 3.x 기본 캐릭터 셋 설명
# Python 3.x 입력 인코딩
print(sys.stdin.encoding)

# Python 3.x 출력 인코딩
print(sys.stdout.encoding)

print('----------------\n')

# 출력문
print("My name is Goodboy!")

# 변수선언
myName = "Goodboy"

# 조건문
if myName == 'Goodboy':
	print("OK")

# 반복문(구구단)
for i in range(2, 10):
	for j in range(1, 10):
		print('%d * %d = ' % (i, j), i * j)

print('----------------\n')

# 변수선언(한글)
이름 = '오호오'
print(이름)

# 함수선언(한글명)
def 인사():
	print("안녕하세요~")
# 함수 실행
인사()

print('----------------\n')

# 클래스 선언
class Cookie:
	pass

# 객체 생성
Cookie = Cookie()
# 정보 값 출력
print(id(Cookie))
print(dir(Cookie))
print(Cookie.__class__)
print(Cookie.__hash__)








