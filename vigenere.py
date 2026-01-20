# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 05:50:27 2022

@author: rjkle
"""

#Vigniere Cipher
#uses a repeating keyword to create an offset to code the message
#use all capital letters and no spaces for the keyword and message

#message = 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'
#keyword = 'PANGRAM'

message = 'BOBKLEMMWONSTATEHEISCOOL'
keyword = 'BANANA'

def encodevigenere(message, keyword):
    code = ''
    char_count = 0
    for char in message:
        index = char_count % len(keyword)
        bcode = ord(keyword[index]) - 65 #0-25 num for the keyword's letter
        acode = ord(char) - 65 #0-25 num for the the message's letter
        new_char_num = (acode + bcode) % 26
        new_char = chr(new_char_num + 65)
        code += new_char
        char_count += 1
    return code


def decodevigenere(code, keyword):
    message = ''
    char_count = 0
    for char in code:
        index = char_count % len(keyword)
        bcode = ord(keyword[index]) - 65 #0-25 num for the keyword's letter
        acode = ord(char) - 65 #0-25 num for the the message's letter
        new_char_num = ((acode - bcode) + 26) % 26
        new_char = chr(new_char_num + 65)
        message += new_char
        char_count += 1
    return message



code = encodevigenere(message, keyword)
print(code)
message = decodevigenere(code, keyword)
print(message)




