# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 07:59:43 2022

@author: rjkle
"""

#Caesar Cipher
#a-z = 0-25
#offset rotates all letters by that amount of the alphabet

#message = 'The quick brown fox jumps over the lazy dog.'
#offset = 3 

message = 'canadian bacon'
offset = 13

def decodecaesar(code, offset):
    message = ''
    for char in code:
        acode = ord(char) #should return 97 thur 122 for lowercase alphabet
        if acode > 64 and acode < 91: #uppercase alphabet
            acode -= offset 
            if acode < 65:
                acode += 26
            new_char = chr(acode)
        elif acode > 96 and acode < 123: #lowercase alphabet
            acode -= offset
            if acode < 97:
                acode += 26
            new_char = chr(acode)
        else: #everything else
            new_char = char
        message += new_char
    return message


def encodecaesar(message, offset):
    code = ''
    for char in message:
        acode = ord(char) #should return 97 thur 122 for lowercase alphabet
        if acode > 64 and acode < 91: #uppercase alphabet
            acode += offset 
            if acode > 90:
                acode -= 26
            new_char = chr(acode)
        elif acode > 96 and acode < 123: #lowercase alphabet
            acode += offset
            if acode > 122:
                acode -= 26
            new_char = chr(acode)
        else: #everything else
            new_char = char
        code += new_char
    return code

code = encodecaesar(message, offset)
print(code)
message = decodecaesar(code, offset)
print(message)



