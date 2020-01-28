# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME형식 - text/csv

# 파이썬 기본 제공 패키지 csv 파일 관련된 함수들 모음
import csv

# Ex. 1
with open('./resource/sample1.csv', 'r') as f:
	reader = csv.reader(f)
	# next(reader)  # Header(컬럼명) 스킵(패스)
	# 확인
	print(reader)
	print(type(reader))
	print(dir(reader))  # 어떤 메소드들이 있는지 확인
	print()

	for c in reader:
		print(c)


# Ex. 2
with open('./resource/sample2.csv', 'r') as f:
	reader = csv.reader(f, delimiter='|')  # delimiter='' 사이에 구분자를 넣어주면 됨
	# next(reader)  # Header(컬럼명) 스킵(패스)
	# 확인
	print(reader)
	print(type(reader))
	print(dir(reader))  # 어떤 메소드들이 있는지 확인
	print()

	for c in reader:
		print(c)

print()

# Ex. 3 (Dict변환)
with open('./resource/sample1.csv', 'r') as f:
	reader = csv.DictReader(f)

	for c in reader:
		# print(c)
		for k, v in c.items():
			print(k, v)
		print('----------------')


# Ex. 4 
w = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18] ]
with open('./resource/sample3.csv', 'w', newline='') as f:
	wt = csv.writer(f)

	for v in w:
		wt.writerow(v)


# Ex. 5
with open('./resource/sample4.csv', 'w', newline='') as f:
	wt = csv.writer(f)
	wt.writerows(w)


# XSL, XLSX
# 파이썬에서 엑셀 관련 처치를 할 때 좋은거
# openpyxl, xlswriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용 !! (openpyxl, xlrd를 내부적으로 사용)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname = '시트명' 또는 숫자, header = 숫자, skiprow = 숫자 --> 줄 수 있는 옵션
xlsx = pd.read.excel('./resource/sample.xlsx')

# 상위 데이터 확인  처음부터 5개
print(xlsx.head())

# 하위 데이터 확인  마지막부터 5개
print(xlsx.tail())

# 행, 열 데이터 확인
print(xlsx.shape)

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.xlsx', index=False)

