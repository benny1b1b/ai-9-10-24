# .2 מחרוזות בסיס -
# ייצר מחרוזת )אחת( של השם המלא שלך ועיר המגורים שלך. הקפד על רווח בין השמות
# a. הדפס את אורך המחרוזת. רמז len
# b. הדפס את המחרוזת כולה באותיות גדולות. רמז upper
# c. הדפס את המחרוזת כולה באותיות קטנות. רמז lower
# d. בדוק אם המחרוזת מתחילה בשם הפרטי שלך. רמז startswith
# e. בדוק אם המחרוזת מסתיימת בעיר המגורים שלך. רמז endswith
# f. פרק את המחרוזת לרשימה המכילה את שמך הפרטי, משפחה, עיר מגורים. רמז split
# g. הפוך את הרווחים לכוכביות. רמז replace. לאחר מכן - פרק שוב את המחרוזת החדשה
# לרשימה )כמו בסעיף הקודם (
# h. הדפס את המחרוזת במרכז של 50 תווים, עטופה בתו "=". רמז center
# i. הדפס את המחרוזת מהתו ה- 4 ועד הסוף
# j. הדפס את המחרוזת מתחילתה ועד לתו ה- 4 )כולל(
# k. הדפס את כל התווים הזוגיים במחרוזת
# l. דאג שכל מילה במחרוזת תתחיל באות גדולה. רמז title
from os.path import split

# ייצר מחרוזת )אחת( של השם המלא שלך ועיר המגורים שלך. הקפד על רווח בין השמות
personal_details = "benny babadjanov ramle"
# a. הדפס את אורך המחרוזת. רמז len
print(len(personal_details))
# b. הדפס את המחרוזת כולה באותיות גדולות. רמז upper
print(personal_details.upper())
# c. הדפס את המחרוזת כולה באותיות קטנות. רמז lower
print(personal_details.lower())
# d. בדוק אם המחרוזת מתחילה בשם הפרטי שלך. רמז startswith
print(personal_details.startswith("Benny"))
# e. בדוק אם המחרוזת מסתיימת בעיר המגורים שלך. רמז endswith
print(personal_details.endswith("Ramle"))
# f. פרק את המחרוזת לרשימה המכילה את שמך הפרטי, משפחה, עיר מגורים. רמז split
print(personal_details.split())
# g. הפוך את הרווחים לכוכביות. רמז לאחר מכן - פרק שוב את המחרוזת החדשה
# לרשימה כמו בסעיף הקודם
print(personal_details.replace(" ", "*"))
print(personal_details.split())
# h. הדפס את המחרוזת במרכז של 50 תווים, עטופה בתו "=". רמז center
print(personal_details.center(50,'='))
# i. הדפס את המחרוזת מהתו ה- 4 ועד הסוף
print(personal_details[4:])
# j. הדפס את המחרוזת מתחילתה ועד לתו ה- 4 )כולל(
print(personal_details[:4+1])
# k. הדפס את כל התווים הזוגיים במחרוזת
print(personal_details[::2])
# l. דאג שכל מילה במחרוזת תתחיל באות גדולה. רמז title
print(personal_details.title())
