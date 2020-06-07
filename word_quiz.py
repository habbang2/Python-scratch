# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:11:59 2020

@author: user
"""


in_file = open('C:/Users/user/Desktop/CODE IT_프로그래밍 기초 강의/실습과제/vocabulary.txt', 'r')

for line in in_file:
    
    word = line.strip().split(": " )
    korean = word[0]
    english = word[1]
    user_answer = input("%s: " % (korean))
    if user_answer == english:
        print("맞았습니다.")
    else:
        print("아쉽습니다. 정답은 %s 입니다." % (english))
        
in_file.close()  
        