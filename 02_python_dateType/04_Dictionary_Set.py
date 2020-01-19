# 딕셔너리 & 집합

# Dictionary : 순서x, 중복x(키에 관해서), 수정o, 삭제o
# Key, Value 형식 (json 형식)  -> MongDB (형식이 비슷함)

# 선언  어떤 데이터 값을 넣어도 가능함 (리스트, 튜플, boolean, int, Strig, ... )
a = {
	'name': 'Kim',
	'Phone': 'xxx-xxxx-xxxx',
	'birth': 123123
	# 'name': 'dddd' 중복 불가
}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = { 'arr': [1, 2, 3, 4, 5] }

# print(type(a))  # 해당 값의 타입 검사

# 출력
print(a['name'])  # a의 name키에 값이 뭐냐 라는 의미
print(a.get('name'))
print(a.get('address'))  # 조회 할때 안정성을 위해서는 get이 좋다 get이 아니였으면 에러 출력...
print(c['arr'][1:2])  # 키를 가진 값을 가져온 후 그게 리스트 여서 슬라이싱 가능

# Dict 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]  # List 추가
a['rank2'] = (1,2,3,)  # Tuple 추가
print(a)

print('---------------------\n')

# Keys, Values
print(a.keys())  # Key 만 출력
print(list(a.keys()))

temp = list(a.keys()) # a딕셔너리의 키값만 리스트로 만듬
print(temp[1:3])

print(a.values()) # 값만 출력
print(list(a.values()))

print('---------------------\n')

# Items(Key, Value 합친 것)
print(list(a.items())) # 리스트 안에 Tuple로 반환

print( 1 in b )  # b중에 Key가 1인 원소가 있니?
print( 2 in b )  # b중에 Key가 2인 원소가 있니?
print( 'name2' not in a ) # a중 Key가 'name2'로 된게 있니?

print('---------------------\n')

# Set (집합) (순서x, 중복x)
# 코딩 형태는 리스트랑 비슷함
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)  # 6이 하나만 출력됨 (교집합 같은 개념)

# 슬라이싱 가능함 -> 튜플이나 리스트로 변환해서..
# 주로 변환해서 사용함
t = tuple(b)
print(t)
l = list(b)
print(l)

print('---------------------\n')

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 겹치는 부분 출력(교집합) intersection, & 둘 다 사용 가능
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 출력  --> 중복 원소 한번만 출력
print(s1 | s2)
print(s1.union(s2))

# 차집합 출력  --> 겹치는 부분 제거
print(s1 - s2)
print(s1.difference(s2))

print('---------------------\n')

# 추가
s3 = set([7, 8, 10, 15])

s3.add(18)
# s3.add(7)  # 이미 존재해서 더이상 추가 안됨
print(s3)

# 제거
s3.remove(15)
print(s3)

print(type(s3))
