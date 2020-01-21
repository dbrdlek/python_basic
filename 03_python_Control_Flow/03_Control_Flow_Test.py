# Python Control Flow Test

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if '가을' in q1.keys():
	print('1.', q1.get('가을'))
	print('1.', q1['가을'])
else:
	print('1. 가을이 없습니다.')

for k in q1.keys():
	if k == '가을':
		print('1.', q1[k])

for k, v in q1.items():
	if k == '가을':
		print('1.', v)



# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

if '사과' in q2.keys() or '사과' in q2.values():
	print('2. 사과가 포함되어 있습니다.')
else:
	print('2. 사과가 포함되어 있지 않습니다.')

for k, v in q2.items():
	if v == '사과':
		print('2.',k, v)
		break
else:
	print('사과 없음')


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 40
if score >= 81:
	print('3. A학점입니다')
elif score >= 61:
	print('3. B학점입니다')
elif score >= 41:
	print('3. C학점입니다')
elif score >= 21:
	print('3. D학점입니다')
else:
	print('3. E학점입니다')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
q4_1 = 12
q4_2 = 6
q4_3 = 18

best = q4_1

if q4_1 > q4_2 and q4_1 > q4_3:
	print('4. q4_1이 제일 크다.')
elif q4_2 > q4_1 and q4_2 > q4_3:
	print('4. q4_2가 제일 크다.')
else:
	print('4. q4_3이 제일 크다.')

if q4_2 > best:
	best = q4_2
if q4_3 > best:
	best = q4_3
print('4. best :', best)

s = '123456-2000000'
# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
id_num = 3000000
str5 = str(id_num)
if str5[0] == '1' or str5[0] == '3':
	print('5. 남자입니다.')
elif str5[0] == '2' or str5[0] == '4':
	print('5. 여자입니다.')
else:
	print("5. 다시 입력 해주세요.")

if int(s[7]) % 2 == 1:
	print('남자')
else:
	print('여자')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "정", "병", "을"]
for l in q3:
	if l == '정':
		continue
		# q3.remove('정')
		# print(q3)
		# break
	else:
		print(l, end='')
print()

# List Comprehension
q5 = [x for x in q3 if x != '정']
print(q5)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
# for num in range(-1, 101, 2):
# 	if num >= 0:
# 		print('7.', num)

for num in range(1, 101):
	if num % 2 == 0:
		continue
	else:
		print(num, end=', ')
print()

for num in range(1, 101):
	if num % 2 != 0:
		print(num, end=', ')
print()
print('---------------------')

q6 = [x for x in range(1, 101) if x % 2 != 0]
print(q6)


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for str_8 in q4:
	if len(str_8) >= 5:
		print(str_8, end='')
print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for lower in q5:
	if lower == lower.lower():
		print('9.', lower)

for v in q5:
	if v.islower():
		print(v, end=' ')
print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for l in q6:
	if l == l.lower():
		print('10.', l.upper())
	else:
		print('10.', l.lower())

# List Comprehension (리스트 컴프리핸션)
# 일반적인 방법
numbers = []
for n in range(1,101):
	numbers.append(n)
print(numbers)
# List Comprehension (리스트 컴프리핸션) 방법
numbers2 = [x for x in range(1, 101)]
print(numbers2)

# Comprehension 형태
# x = [새로 담을 변수(조건식이 있으면 참값만) for 반복되는 변수 in 반복횟수(시퀀스가 있는 객체) if 조건문]

