import datetime

my_birthday = "Feb 18, 2005"
my_birthday2 = "2005-02-18"

today = datetime.date.today()

today_plus_30 = today + datetime.timedelta(days=30)

print("Today is:", today)
print("30 days from today is:", today_plus_30)
