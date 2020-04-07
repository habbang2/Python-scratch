# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:21:42 2020

@author: user
"""


#변수지정
n = 120
i = 1
count = 0 

while  i <= 120:
    if n % i == 0:
        print(i)
        count = count + 1
    i = i + 1


#f-string으로 할경우
print(f"{n}의 약수는 총 {count}개입니다.")

#format method로 할 경우
print("{}의 약수는 총 {}개입니다.". format(n,count))