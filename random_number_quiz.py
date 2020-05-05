# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:15:22 2020

@author: user

"""


from random import randint
answer = randint(1, 20)

i = 0


while i < 4:
    number = input(f"기회가 {4-i}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요:")
    
  
    if int(number) < answer:
        print("up")
    elif int(number) > answer:
        print("Down")
    elif int(number) == answer:
        print(f"축하합니다.{i+1}번만에 숫자를 맞추셨습니다.")
        break
   
    
    i = i + 1
    
    if i >= 4 :  
        print(f"아쉽습니다. 정답은 {answer}였습니다.")
        
        