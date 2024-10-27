# .1 רשימות תנאים בולייאנים-
# a. ייצר רשימה בת 3 איברים ושים בתוכה ערכים אקראיים
# random choice - ב השתמש True False של
# b. בפעולה אחת בדוק והדפס האם כל הרשימה מכילה רק True
# c. בפעולה אחת בדוק והדפס האם הרשימה מכילה לפחות True אחד
# d. בפעולה אחת בדוק והדפס האם כל הרשימה מכילה רק False
# e. בפעולה אחת בדוק והדפס האם הרשימה מכילה לפחות False אחד
# f. ייצר רשימה אקראית של חמישה מספרים בין 2 למינוס 2 )כלומר ,2 ,1 ,0 -1 , -2(
# השתמש בפונקציות random
# g. בפעולה אחת בדוק והדפס האם כל הרשימה מכילה רק מספרים שונים מ- 0
# h. בפעולה אחת בדוק והדפס האם הרשימה מכילה לפחות איבר אחד שהוא לא 0
# i. בפעולה אחת בדוק והדפס האם כל הרשימה מכילה רק- 0
# j. בפעולה אחת בדוק והדפס האם הרשימה מכילה לפחות איבר אחד שהוא 0
import random


# a. ייצר רשימה בת 3 איברים ושים בתוכה ערכים אקראיים
# random choice - ב השתמש True False של
list_rbool3:list[bool] = [random.choice([True,False]) for _ in range(3)]
#b
print("all True?", list_rbool3, all(list_rbool3)) #מדפיס אמת אם כל האיברים אמת
#c
print("any True?", list_rbool3, any(list_rbool3)) # מדפיס אמת אם איבר אחד לפחות אמת
#d
print("all False?", list_rbool3, not any(list_rbool3)) # מדפיס אמת אם אף איבר אינו אמת
#e
print("any False?", list_rbool3, not all(list_rbool3)) # מדפיס אמת אם לא כל האיברים ברשימה הם אמת או לפחות איבר אחת הוא שקר
#f
list_rand5: list[int] = [random.randint(-2,2)for i in range(5)]
print(list_rand5)
#g  בפעולה אחת בדוק והדפס האם כל הרשימה מכילה רק מספרים שונים מ- 0
print("all different 0?",all(list_rand5))
#h בפעולה אחת בדוק והדפס האם הרשימה מכילה לפחות איבר אחד שהוא לא 0
print("any not 0?", any(list_rand5))
#i בפעולה אחת בדוק והדפס האם כל הרשימה מכילה רק- 0
print("all 0?", not any(list_rand5)) # מדפיס אמת אם אף לא אמד מהרשימה הוא אמת- משמע כולם הם שקר
#j 0 בפעולה אחת בדוק והדפס האם הרשימה מכילה לפחות איבר אחד שהוא
print("any 0?", not all(list_rand5)) # מדפיס אמת אם לא כל האיברים ברשימה הם אמת- משמע יש לפחות שקר אחד
