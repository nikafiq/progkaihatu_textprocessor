import sys
import re
import chardet
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() #no full GUI
testfile = askopenfilename() #show an "Open" dialog box
#testfile = 'test.txt' #temporary filepath for testing purpose

print("Your test file is: "+testfile)
print(open(testfile, 'r').read)
with open(testfile, 'rb') as f:
    #print("The txt file contain: "+f.read(testfile))
    print(chardet.detect(f.read()))
    f.close()

test_str = testfile
with open(test_str, 'r') as file:
    print(file)
