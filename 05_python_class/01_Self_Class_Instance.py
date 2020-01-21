# 파이썬 클래스 상세이해
# Self, Class, instance Val

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 각가의 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재

# 형식
# class 클래스명:
#   속성, 메소드로 구성
# 	함수
# 	함수
# 	함수
# __ 로 시작하는 함수들은 매직 메소드

# 선언
# Ex. 1
class UserInfo():
	# 속성, 메소드
	def __init__(self, name):
		self.name = name
		# print('초기화 : ', name)
	def user_info_p(self):
		print('Name : ', self.name)

# nameSpace 네임스페이스
# 인스턴스가 갖고있는 자기 자신의 저장 공간
user1 = UserInfo('Kim')
user1.user_info_p()
user2 = UserInfo('Park')
user2.user_info_p()

print(id(user1))  # id는 메모리 주소 확인하는 함수
print(id(user2))
print(user1.__dict__)
print(user1.__dict__)

# Ex. 2
# self의 이해
# class SelfTest():
# 	# 클래스 메소드
# 	def function1():
# 		print('function1 called!')
	
# 	# 인스턴스 메소드
# 	def function2(slef):
# 		print(id(slef))
# 		print('function2 called!')

# self_test = SelfTest()
# # self_test.function1()
# SelfTest.function1()
# self_test.function2()

# print(id(self_test))  # 인스턴스 한 id값과 똑같다
# SelfTest.function2(self_test)

# Ex. 3
# 클래스 변수(self x), 인스턴스 변수(self가 들어간다)
class WareHouse:
	# 클래스 변수
	stock_num = 0

	def __init__(self, name):
		self.name = name
		WareHouse.stock_num += 1
	def __del__(self):
		WareHouse.stock_num -= 1

user1 = WareHouse('kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)  # 클래스 네임스페이스, 클래스 변수 공유

print(user1.name)
print(user2.name)
print(user3.name)
# 자기 네임스페이스에 없으면 클래스 네임스페이스에서 찾고 거기서도 없으면 에러 발생
print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

# user1 삭제
del user1
# print(user1.stock_num) 위에 del함수로 인스턴스 삭제됨
print(user2.stock_num)
print(user3.stock_num)

