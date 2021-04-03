# Section11
# 좀 빡세게 복습
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) # 첫 번째 줄에 있는 값의 분류(Header)를 한줄 건너뛰어 뛰어줌으로 데이터들만 불러옴
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)
    
# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|') # delimiter ''안의 값으로 분리 시켜줌
    # next(reader) Header 스킵
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)   

# 예제3 (Dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('---------------')    

# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# 예제5
# for 문을 쓰지 않고 한번에 쓰는법

with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)

# XSL, XLSX
# openpyxl, xlswriter, xlrd, xlwt, xlutils
# pandas를 주로사용(openpyxl + xlrd) 
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

xlsx = pd.read_excel('./resource/sample.xlsx') # 파일 경로 끝 , 뒤에
# sheetname='시트명' 또는 숫자, header=3(첫줄로 만들 행), skiprow=숫자(가져오지 않을 행)
# 엑셀 파일 하나에 여러 시트가 있을 경우 sheetname
# 상위데이터 확인
print(xlsx.head())
print()

# 끝부분 데이터 확인
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape) # 행, 열

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index = False)
xlsx.to_csv('./resource/result.csv', index = False)







