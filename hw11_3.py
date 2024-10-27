# .3 מחרוזות חלק ב' -
# a. הסר את הרווחים משני הצדיים של המחרוזת הבאה : " day-fun "
# b. בדוק אם המחרוזת "hello "מכילה אותיות בלבד. רמז isalpha
# c. בדוק אם המחרוזת "777" מכילה מספרים בלבד. רמז isdigit
# d. בדוק אם המחרוזת " " מכילה רווחים בלבד. רמז isspace
# e. עבור הרשימה ['A ','J ','N ','I ','N['. צור ממנה מחרוזת אחת. רמז join
# f. עבור אותה הרשימה- צור מחרוזת אחת עם '*' בין התווים. A*J*N*I*N. רמז join
# g. תוך התעלמות מאותיות גדולות וקטנות: בדוק אם האות e מופיעה במילה hELLo
# in, lower :רמז
# h.* בונוס: קלוט מילה מהמשתמש, ואז באמצעות comprehension ייצר רשימה המכילה
# כל אות כאיבר . כל אות תהיה גדולה. התעלם מספרות
# ['P', 'Y', 'T', 'H', 'O', 'N'] תהיה התוצאה py3thon12 - עבור לדוגמא


# a. הסר את הרווחים משני הצדיים של המחרוזת הבאה : " day-fun "
text: str = " day-fun "

print(text.strip())
# b. בדוק אם המחרוזת "hello "מכילה אותיות בלבד. רמז isalpha
text1: str = "hello"
print(text1.isalpha())
# c. בדוק אם המחרוזת "777" מכילה מספרים בלבד. רמז isdigit
text2: str = "777"
print(text2.isdigit())
# d. בדוק אם המחרוזת " " מכילה רווחים בלבד. רמז isspace
text3: str = "  "
print(text3.isspace())
# e. עבור הרשימה ['A ','J ','N ','I ','N['. צור ממנה מחרוזת אחת. רמז join
list_ninja: list[str] = ['N' ,'I' ,'N' ,'J' ,'A']
print(''.join(['N', 'I', 'N', 'J', 'A']))
# f. עבור אותה הרשימה- צור מחרוזת אחת עם '*' בין התווים. A*J*N*I*N. רמז join
print('*'.join(['N', 'I', 'N', 'J', 'A']))
# g. תוך התעלמות מאותיות גדולות וקטנות: בדוק אם האות e מופיעה במילה hELLo
# in, lower :רמז
x: str = "e"
word: str = "hELLo"
print(x.upper() in word.upper())
# h.* בונוס: קלוט מילה מהמשתמש, ואז באמצעות comprehension ייצר רשימה המכילה
# כל אות כאיבר . כל אות תהיה גדולה. התעלם מספרות
# ['P', 'Y', 'T', 'H', 'O', 'N'] תהיה התוצאה py3thon12 - עבור לדוגמא

word1: str = "py3thon12"
pixed_word1: list[str] = [char.upper() for char in word1 if not char.isdigit()]
print(pixed_word1)
