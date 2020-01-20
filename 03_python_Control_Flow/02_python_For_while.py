# For_While (반복문)

# 코딩 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
	print("v1 is :", v1)
	v1 += 1
else:
	pass

for v2 in range(10):
	print("v2 is :", v2)
	pass

for v3 in range(1, 10):
	print('v3 is :', v3)
	pass

print('--------------------\n')

# 1 ~ 100 sum
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
	sum1 += cnt1
	cnt1 += 1

print('1 ~ 100 : ', sum1)
print('1 ~ 100 : ', sum(range(1, 101)))
print('1 ~ 100 : ', sum(range(1, 101, 2)))  # 1 ~ 100 까지 중에 2개 단위로 건너뛰면서

print('--------------------\n')

# 시퀀스(순서가 있는)자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전  -> 반복 가능
# iterable 리턴 가능 함수 : range, reversed, enumerate, filter, map, zip
names = ['Kim', 'Park', 'Cho', 'Choi', 'Yoo']

for name in names:
	print("You are : ", name)

word = 'dreams'
for s in word:
	print("Word : ", s)

print('--------------------\n')

my_info = {
	'name': 'Kim',
	'age': 33,
	'city': 'Seoul'
}
# 기본 값은 키
for key in my_info:
	print('my_info', key)

print('--------------------\n')

# 값
for key in my_info.values():
	print('my_info', key)

print('--------------------\n')

# 키
for key in my_info.keys():
	print('my_info', key)

print('--------------------\n')

# 키 & 값
for k, v in my_info.items():
	print('my_info', k, v)

print('--------------------\n')

# 소문자는 대문자로 대문자는 소문자로
name = "KennRY"
for n in name:
	if n.isupper():
		print(n.lower())
	else:
		print(n.upper())

print('--------------------\n')

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# print(33 in numbers)
for num in numbers:
	if num == 33:
		print('found : 33~')
		break
	else:
		print('not found : 33!')

print('--------------------\n')

# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
for num in numbers:
	if num == 33:
		print('found : 33!')
		break
	else:
		print('not found : 33!')
else:
	print('not found 33.......')

print('--------------------\n')

# continue 를 만나면 다음 순회할 인덱스로 간다(패스하는 느낌)
lt = ['1', 2, 5, True, 4.3, complex(4)]

for v in lt:
	if type(v) is float:
		continue
	print('Type : ', type(v))		

print('--------------------\n')

# 자료구조 변환
name = 'Niceman'
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))