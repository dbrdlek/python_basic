# 테이블 데이터 수정 및 삭제

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pkg._DB_INFO import DbConn as dbConn

# Cursor 연결
c = dbConn().cursor()

# 데이터 수정 1
# c.execute('UPDATE users SET username = ? WHERE id = ?', ('niceman', 2))

# 데이터 수정 2
# c.execute('UPDATE users SET username = :name WHERE id = :id', {'name': 'goodman', 'id' : 5})

# 데이터 수정 3
# c.execute('UPDATE users SET username = "%s" WHERE id = "%d"' % ('Badboy', 3))

# 중간 데이터 확인
for user in c.execute('SELECT * FROM users'):
	# print(user)
	pass

# Row DELETE 1
c.execute("DELETE FROM users WHERE id = ?", (2, ))

# Row DELETE 2
c.execute("DELETE FROM users WHERE id = :id", {'id': 5} )

# Row DELETE 3
c.execute("DELETE FROM users WHERE id = '%s'" % 4 )

# 중간 데이터 확인 2
for user in c.execute('SELECT * FROM users'):
	print(user)

# 테이블 전체 데이터 삭제
print('users db delete : ', dbConn().execute("DELETE FROM users").rowcount, ' rows')

# 커밋
# dbConn().commit() 오토커밋 중

# 접속 해제
dbConn().close()








