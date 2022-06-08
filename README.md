# progkaihatu_textprocessor
A program to read your txt file and differentiate character encoding, number, string and newlines\
Running the program in your python IDE will prompt you to open txt file

**This is the result of running the program using the sample *text.txt* file**
```
 Your test file is: text.txt
 {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

 Your txt file contain: 
 これはひらがなでかかれています
 カタカナテスト
 漢字試験
 Ｆｕｌｌ　ｓｉｚｅ　ｃｈａｒａｃｔｅｒ　ｔｅｓｔ
 This is a half sized character line
 0123456789

 The half-width character in the txt file is:
 ['This', 'is', 'a', 'half', 'sized', 'character', 'line']

 The half-width number in the txt file is:
 ['0123456789']

 The full-width character in the txt file is:
 ['これはひらがなでかかれています', 'カタカナテスト', 'Ｆｕｌｌ', 'ｓｉｚｅ', 'ｃｈａｒａｃｔｅｒ', 'ｔｅｓｔ']

 The full-width character in the txt file is:
 ['漢字試験']
```