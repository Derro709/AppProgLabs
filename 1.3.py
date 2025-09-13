year = int(input())
print('високосный') if year%4==0 and (year%100!=0 or year%400==0) else print('не високосный')
