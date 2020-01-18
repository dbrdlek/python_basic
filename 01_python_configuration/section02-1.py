# Section02-1
# 파이썬 기초 코딩
# pirnt 구문의 이해
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
  \n : 개행
  \t : 탭
  \\ : \문자 출력
  \' : '문자 출력
  \" : "문자 출력
  \r : 개리지 리턴
  \f : 폼 피드
  \a : 벨 소리
  \b : 백 스페이스
  \000 : 널 문자
"""

# 기본 출력
print('Hello Python!')  # 문법적 중요
print("Hello Python!")  # 텍스트 의미
print("""Hello Python""")
print('''Hello Python''')

print('---------------\n')

# separator 옵션 이용
# sep 사용하면 문자 사이에 공백을 ''사이로 맞춰중
print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='')
print('niceman', 'google.com', sep='@')

print('---------------\n')

# end 옵션 사용
# 기본 print 문을 사용하면 개행이 되는데 end ''사이 글자로 붙여서 사용됨
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes') # end 종료 후
print('end 문 끝')

print('---------------\n')

# file 옵션 사용
import sys

print('GeeksForGeeks', file=sys.stdout)

print('---------------\n')

# 서식 문자
print("%s's favorite number is %d" % ('Eunki', int(45)))
# format 사용
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{var1} are {var2}'.format(var1='You', var2="Niceman"))
# format 응용
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test2: {0:5d}, Price:{1: 4.2f}".format(776, 6534.123))
print("Test3: {a:5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))




