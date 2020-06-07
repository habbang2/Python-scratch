# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:37:12 2020

@author: user
"""


out_file = open('vocabulary.txt', 'w')

while True:
    english = input("영어 단어를 입력하세요:")
    if english == "q":
        break
    
    korean = input("한국어 뜻을 입력하세요:")
    if korean == "q":
        break
    
    #out_file.write(f"{english}: {korean}\n")
    out_file.write("%s: %s\n" % (english, korean))
    

out_file.close()