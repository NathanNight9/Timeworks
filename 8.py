from datetime import date

a_year = int(input())
a_month = int(input())
a_day = int(input())

date_a = date(a_year, a_month, a_day)

date_b = date.today()

print(((date_b - date_a).days) / 365)