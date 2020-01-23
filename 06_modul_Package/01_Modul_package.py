# python 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 폴더를 다르게 구분해놔서 한번에 import가 안돼 
# os, sys에 path를 추가함
# 아니면 이 폴더 안에 pkg폴더가 있으면 사용 가능함
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# import sys
# print(sys.path)

# 사용1(클래스)
from pkg.fibonacci import Fibonacci
# from pkg.calculations import calculations

Fibonacci.fib(300)

print('ex1 :', Fibonacci.fib2(400))
print('ex1 :', Fibonacci().title)

# 사용2(클래스)
# 권장하진 않음 모두 가져오는것
from pkg.fibonacci import *

Fibonacci.fib(500)

print('ex2 :', Fibonacci.fib2(600))
print('ex2 :', Fibonacci().title)

# 사용3(클래스)
# 사용할 이름을 바꾸는 것
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

print('ex3 :', fb.fib2(600))
print('ex3 :', fb().title)

# 사용4(함수)
import pkg.calculations as c

print('ex4 :', c.add(10, 100))
print('ex4 :', c.mul(10, 100))

# 사용5(함수)
# 필요한 함수만 사용하는거
# 이걸 권장  --> 리소스 낭비 방지
from pkg.calculations import div as d

print('ex5 :', int(d(100, 10)))

# 사용 6
import pkg.prints as p
# python 기본적으로 가지고 있는 내장함수
import builtins

p.prt1()
p.prt2()
# print(dir(builtins))  # 어떤 함수들이 있는지 확인하는 법





