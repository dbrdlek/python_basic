def prt1():
	print("I'm Boy!")

def prt2():
	print("I'm Good!")

# 단위 실행(독립적으로 파일을 실행)
# 파이썬 2.x 버전일때 자주 쓰임
# main 일때만 실행하는 거라 다른 폴더/파일 에서 import할 경우 실행 되지 않음
# 단위 테스트 --> 독립적으로 이 코드들이 잘 실행 되는지 확인할 때 쓰임
if __name__ == "__main__":
	prt1()
	prt2()