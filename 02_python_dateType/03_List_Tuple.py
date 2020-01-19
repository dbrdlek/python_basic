# Python Date Type(자료형)
# List, Tuple

# List( 순서 O, 중복O, 수정O, 삭제O )

# 선언
a = []
b = list()
c = [1, 2, 3, 4]  # 정수 리스트
d = [10, 100, 'Pen', 'Banana', 'Orange']  # 정수 + 숫자 리스트
e = [10, 100, ['Pen', 'Banana', 'Orange']] # 정수 + 숫자 + 리스트추가한 리스트

# 인덱싱
print( d[3] )
print( d[-2] )
print( d[0] + d[1] )
print( e[2][1] )
print( e[-1][-2] )

print('-------------------\n')

# 슬라이싱
print( d[0:2] )  # List로 반환해서 0번째부터 2번째 인덱스까지 호출
print( e[2][1:3] )

# 연산
print(c + d) # 하나의 리스트로 확장된다.
print(c * 3) # c 리스트 3번 확장(extend)
print( str( c[0] ) + 'hi' )  # 형 변환 후 문자 추가

print('-------------------\n')

# 리스트 수정
c[0] = 77 # c의 0번째 인덱스 77로 수정
print(c) 
c[1:2] = [100, 1000, 10000] # c 리스트에서 1부터 2사이 구간에 삽입된다
print(c)
c[1] = ['a', 'b', 'c']  # List 안에 리스트 추가
print(c)

# 리스트 삭제
del c[1]  # 해당 인덱스 삭제
print(c)
del c[-1]
print(c)

print('-------------------\n')

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)  # 끝 부분에 원소 추가
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7)  # 2번 인덱스를 7추가
print(y)
y.remove(2)  # 2번 인덱스를 지우는게 아니라 데이터의 값이 2인것을 삭제
y.remove(7)
print(y)
y.pop()  # 마지막 원소 삭제  --> 이걸 계속 쓰다보면 언젠간 에러가 난다. 그래서 예외처리를 해줘야 할듯,,
print(y)  # LIFO  List In First Out

ex = [88, 77]
y.extend(ex)  # 리스트를 추가하는게 아니라 ex안에 있는 리스트 원소들을 추가
# y.append(ex) # 리스트 자체를 추가
print(y)

# 삭제 : del(해당 인덱스 삭제), remove(해당 값 삭제), pop(제일 마지막 원소 삭제)

print('-------------------\n')

############## 튜플 ######################

# Tuple (순서o, 중복o, 수정x, 삭제x)
# 사용 예제 은행 계좌번호 같이 변경되면 프로그램상 데미지가 있는 것들에 대해 변경 방지

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# 인덱싱
print(c[2])
print(c[3])
print(d[2][2])

print('-------------------\n')

# 슬라이싱
print(d[2:])  # d의 2부터 모두 출력
print(d[2][0:2]) # d의 2에서 0부터 2번째까지
print(c + d)  # 확장 후 하나로 반환
print(c * 3)

print('-------------------\n')

# Tuple 함수
z = (5, 2, 1, 3, 4, 1)

print(z)
print(3 in z)  # 3이 z Tuple 안에 존재 하는지
print(z.index(5))  # 찾고자 하는 값의 인덱스를 반환함
print(z.count(1))  # 찾고자 하는 값의 숫자가 몇개가 있어 라는 뜻이다













