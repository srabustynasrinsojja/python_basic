from datetime import date, datetime
today = date.today()
# dd/mm/yy
d = today.strftime("%d/%m/%y")
print("d=" ,d)

# textual month/mm/yy
d1 = today.strftime("%B,%m/%y")
print("d1 =" ,d1)

from datetime import date
today_date = date.today()
dob = date(2001,1,8)
print(today_date - dob)

from datetime import date
td = date.today()
dob = date(2001,1,8)
age = td - dob 
print("your age is " ,age)

from datetime import date
#current datetime
unaware = datetime.now
print("timezone naive " ,unaware)

