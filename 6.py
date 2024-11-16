from datetime import date

a_year = int(input())
a_month = int(input())
a_day = int(input())

date_a = date(a_year, a_month, a_day)

b_year = int(input())
b_month = int(input())
b_day = int(input()) 

date_b = date(b_year, b_month, b_day)

print((date_b - date_a).days)