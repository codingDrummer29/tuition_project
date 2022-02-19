import datetime

currentDate=datetime.date.today()

print('Day Name: ', currentDate.strftime('%A')) 
print('Month Name: ', currentDate.strftime('%B')) 
print('Day of month: ', currentDate.strftime('%d')) 
print('Day of year: ', currentDate.strftime('%j'))