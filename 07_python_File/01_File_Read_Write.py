# File read, write
# 읽기모드 : r , 쓰기모드(기존 파일 삭제) : w ,
# 추가모드 : a (파일 생성 또는 추가)
# .. : 상대경로, . : 절대 경로
# 참조 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# Ex. 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
# dir() = 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드()를 가지고 있는지 나열
print(dir(f))
# !! 반드시 close 리소스 반환 !!
f.close()

print('---------------------------------')
print('---------------------------------\n')

# Ex. 2
# with 문은 close를 생략해도 괜찮음
with open('./resource/review.txt', 'r') as f:
	c = f.read()
	print(c)
	print(list(c))
	print(iter(c))  # iterator로 반환하기 때문에 for문에서도 사용 가능하다

print('---------------------------------')
print('---------------------------------\n')


# Ex. 3
with open('./resource/review.txt', 'r') as f:
	for c in f:
		print(c.strip())  # 양쪽 공백, 줄바꿈 제거

print('---------------------------------')
print('---------------------------------\n')

# Ex. 4
with open('./resource/review.txt', 'r') as f:
	content = f.read()
	print('>', content)
	content = f.read()  # 이미 읽은 상태라 여기부터 내용이 없다
	print('>', content) # 출력결과 없음

print('\n---------------------------------')
print('---------------------------------\n')

# Ex. 5
with open('./resource/review.txt', 'r') as f:
	line = f.readline()  # --> 한 줄씩 읽어 오는 메소드 (한 문장씩 필요할 땐 이게 더 좋음)
	# print(line)
	while line:
		print(line, end='###')
		line = f.readline()

print('---------------------------------')
print('---------------------------------\n')

# Ex. 6
# readlines는 리스트를 리턴한다
with open('./resource/review.txt', 'r') as f:
	contents = f.readlines()  # 리스트를 리턴한다
	print(contents)
	for c in contents:
		print(c, end=' ***** ')


print('---------------------------------')
print('---------------------------------\n')

# Ex. 7
# score 파일 평균 구하기
score = []
with open('./resource/score.txt', 'r') as f:
	for line in f:
		score.append(int(line))   # txt 파일은 모두 문자열이라 int로 형변환
	print(score)
print('Average : {:6.3}'.format(sum(score)/len(score)))


# 파일 쓰기

# Ex. 1
# w는 쓰기
with open("./resource/test1.txt",'w') as f:
	f.write('Niceman!\n')

# Ex. 2
# a = 기존 파일 추가
with open("./resource/test1.txt",'a') as f:
	f.write('Goodman!\n')

# Ex. 3
from random import randint

with open("./resource/test2.txt",'w') as f:
	for cnt in range(6):
		f.write(str(randint(1, 50)))
		f.write('\n')

# Ex. 4
# writelines : 리스트 -> 파일로 저장
with open("./resource/test3.txt",'w') as f:
	list = ['Kim\n', 'Park\n', 'Cho\n']
	f.writelines(list)

# Ex. 5
# 파일로 로그에 관한 것들을 대해서 찍을 때 사용하기 편함
with open('./resource/test4.txt', 'w') as f:
	print('Test Contests1', file=f)
	print('Test Contests1', file=f)





