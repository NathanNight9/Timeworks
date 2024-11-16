from datetime import datetime

Y, M, D = map(int, input().split())
H, Min, S = map(int, input().split())

newdate = datetime(Y, M, D, H, Min, S)
currentdate = datetime.now()
print((currentdate - newdate))
