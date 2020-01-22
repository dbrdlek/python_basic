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





