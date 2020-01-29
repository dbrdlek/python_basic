# 파이썬 데이터베이스 연동(SQLite)

# pkg파일 import 하기 위해 path 추가
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# 로컬 db 경로 지정후 conn
from pkg._DB_INFO import DbConn as dbConn

# 커서 바인딩  커서의 위치가 되게 중요하다
# 다음 데이터의 위치를 기억한다
c = dbConn().cursor()

# 데이터 조회(전체)  -> 총 데이터가 5개 이다
c.execute('SELECT * FROM users')

## 커서 위치가 변경
## 1개 로우 선택
# print('One -> \n', c.fetchone())

## 지정 로우 선택 ->  2, 3, 4 데이터(전에서 커서가 1번 옮겨짐)
# print('Three -> \n', c.fetchmany(size=3))

## 전체 로우 선택 -> 총데이처의 수가 5라서 그렇지 더 많으면 다 가져온다
# print('All -> \n', c.fetchall())
# print('One -> ', c.fetchone()) # None 발생 이거 때문에 위치 중요
# print('All -> ', c.fetchall()) # 빈 리스트 반환

print()


## 순회 1
# rows = c.fetchall()
# for row in rows:
# 	print('retrieve1 > ', row)

# 순회 2 이게 더 많이 쓰임
# for row in c.fetchall():
# 	print('retrieve2 > ', row)

## 순회 3 코드 가독성이 떨어져 2번째 방법을 좀 더 선호
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
# 	print('retrieve2 > ', row)


# WHERE Retrieve1
param1 = (3, ) # 튜플로 바인딩
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) # 데이터 없음

# WHERE Retrieve2
param2 = 4 # 인티져 바인딩
# %s 문자, %f 실수, %d 정수
c.execute('SELECT * FROM users WHERE id="%s"' % param2) 
print('param2', c.fetchone())
print('param2', c.fetchall()) # 데이터 없음

# WHERE Retrieve3
# : --> 딕셔너리 불러올 때 사용
c.execute('SELECT * FROM users WHERE id=:Id' , {'Id': 5})
print('param3', c.fetchone())
print('param3', c.fetchall()) # 데이터 없음

# WHERE Retrieve4
param4 = (3, 5)
# IN은 sql 함수이다 --> List로 반환
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" % (3,4) )
print('param5', c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5} )
print('param5', c.fetchall())


# Dump 이용 --> DB를 백업 하는것이다
# 데이터가 몇먹건 되면 덤프파일이 기가 단위로 된다
# 그래서 처음에 DB클러스터링을 잘해야 된다

# iterdump() -> 테이블, 데이터 모두 sql쿼리로 만들어 준다
with dbConn():
	with open('백업받을 경로', 'w') as f:
		for line in dbConn().iterdump():
			f.write('%s\n' % line)
		print('Dump Print Complete')
# f.close() , dbConn().close()  -> with 문이라 저절도 됨

