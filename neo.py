
from datetime import date


birthOfYear = int(input('Please tell your date of year = '))
currentYear = date.today().year
age = currentYear - birthOfYear
print('Your age is = ', age)
