# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:12:29 2020

@author: user
"""
'''
밑에 나와 있는 data/chicken.txt 파일에는 제가 운영하는 치킨집 '코딩에빠진닭(이하 코빠닭)'의 12월 매출이 정리되어 있습니다. :의 왼쪽에는 며칠인지, 그리고 오른쪽에는 그 날의 매출이 적혀 있습니다.


1일: 453400
2일: 388600
3일: 485300
4일: 477900
5일: 432100
6일: 665300
7일: 592500
8일: 465200
9일: 413200
10일: 523000
11일: 488600
12일: 431500
13일: 682300
14일: 633700
15일: 482300
16일: 391400
17일: 512500
18일: 488900
19일: 434500
20일: 645200
21일: 599200
22일: 472400
23일: 469100
24일: 381400
25일: 425800
26일: 512900
27일: 723000
28일: 613600
29일: 416700
30일: 385600
31일: 472300

data 폴더의 chicken.txt를 읽어 들이고, strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 계산하세요. 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다. 만약 한 달이 28일이거나 30일이면, 그에 맞게 평균 매출을 구할 수 있도록 코드를 짜셔야 합니다.
'''




# 매출 파일 열기


file = open('C:/Users/user/Desktop/basic/chicken.txt', 'r', encoding = 'utf-8')

sum = 0

#줄 세기
line_count = 0

for line in file:
    data = line.strip().split(": ")
    amount = int(data[1])
    
    #각 날의 매출을 총 매출에 추가
    sum = sum + amount
    line_count = line_count + 1
    
print(sum / line_count )
# 파일 닫기

file.close()
