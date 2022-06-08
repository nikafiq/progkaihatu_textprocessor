import os
import re
import chardet
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() #no full GUI
testfile = askopenfilename() #show an "Open" dialog box to choose txt file
#testfile = 'text.txt' #temporary filepath for testing purpose
f = open(testfile)
testpath = os.path.realpath(f.name) #linking file path
teststr = f.read() #saving content in txt file as string

def check_encoding(a): #confirm the txt file encoding
    print("Your test file is: "+a)
    with open(a, 'rb') as f:
        #print("The txt file contain: "+f.read(testfile))
        print(chardet.detect(f.read()), end='\n\n')
        f.close()

def show_txt(): #display the txt file contet
    with open(testpath, 'r') as f2:
        print("Your txt file contain: \n"+ f2.read(), end='\n\n')

def chr_select():
    p = re.compile('[a-zA-Z]+')
    result = p.findall(teststr)
    print("The half-width character in the txt file is:")
    print(result, end='\n\n')

def num_select():
    p = re.compile('[0-9]+')
    result = p.findall(teststr)
    print("The half-width number in the txt file is:")
    print(result, end='\n\n')

def fullchr_select():
    p = re.compile('[あ-んア-ンａ-ｚＡ-Ｚ]+')
    result = p.findall(teststr)
    print("The full-width character in the txt file is:")
    print(result, end='\n\n')

def kanji_select():
    p = re.compile('[\u2E80-\u2FDF\u3005-\u3007\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]+')
    result = p.findall(teststr)
    print("The kanji in the txt file is:")
    print(result, end='\n\n')

check_encoding(testfile)
show_txt()
chr_select()
num_select()
fullchr_select()
kanji_select()
