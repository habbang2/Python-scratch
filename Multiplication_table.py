# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:53:43 2020

@author: user
"""
#구구단을 만들어보세요. while문을 사용하여 콘솔에 아래 문장들이 출력되게 프로그램을 작성하세요.

i = 1

while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} * {j} = {i * j}")
        j = j + 1
    i = i + 1
    