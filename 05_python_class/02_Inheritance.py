# 파이썬 클래스 상세 이해
# 상속, 다중상속
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능
# 상속 장점 코드 재사용, 중복 코드 최소화, 생산성-유지보수(가독성) up
# 예를 들면 -- 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

# Ex. 1
class Car:
	"""Parent Class"""
	def __init__(self, tp, color):
		self.type = tp
		self.color = color
	
	def show(self):
		return 'Car class "Show Method!"'

class BmwCar(Car):
	"""Sub Class"""
	def __init__(self, car_name, tp, color):
		super().__init__(tp, color)
		self.car_name = car_name
	
	def show_model(self) -> None:
		return "Your Car Name : %s" % self.car_name
	

class BenzCar(Car):
	"""Sub Class"""
	def __init__(self, car_name, tp, color):
		super().__init__(tp, color)
		self.car_name = car_name
	
	def show_model(self) -> None:
		return "Your Car Name : %s" % self.car_name

	def show(self):
		print(super().show())  # 같은 메소드 이름의 부모것도 불러 오고 싶을때 하는 법
		return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super(color는 부모의 것에서 가져옴 BmwCar에선 없음)
print(model1.type)  # Super
print(model1.car_name) # Sub (자식)
print(model1.show())  # SuperMethod (부모의 메소드)
print(model1.show_model()) # SubMethod
print(model1.__dict__)

# Method Overriding(메소드 오버라이딩)
# 같은 이름의 메소드를 사용할 때 가능함
# 부모의 있는걸 모두 사용하는게 아니라 자식에서 상속 받을건 받고 기능을 개선, 추가 가능하다.
model2 = BenzCar('220d', 'suv', 'black')
print(model2.show())

# Parent Method Call
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())

# Inheritance Info
# 상속관계가 나타나는 메소드 mro()
# 상속 정보를 List형태로 반환한다.
print(BmwCar.mro())
print(BenzCar.mro())

# Ex.2 
# 다중 상속
# 보통 2개정도 상속받는다
class X():
	pass

class Y():
	pass

class Z():
	pass

class A(X, Y):
	pass

class B(Y, Z):
	pass

class M(B, A, Z):
	pass

print(M.mro())
print(A.mro())

