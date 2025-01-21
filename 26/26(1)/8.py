data = list(map(int, open('8')))
n = 10000
data.sort()
first_sale = 0
second_sale = 0

slice = int(n * 0.7)
first_30_sales = data[:slice]
first_40_sales = data[slice:]
total_sales_1 = 0
for product in first_30_sales:
    total_sales_1 += product * 0.3
for product in first_40_sales:
    total_sales_1 += product * 0.4
profit_1 = sum(data) - total_sales_1

slice = int(n * 0.5)
second_40_sales = data[:slice]
second_35_sales = data[slice:]
total_sales_2 = 0
for product in second_40_sales:
    total_sales_2 += product * 0.4
for product in second_35_sales:
    total_sales_2 += product * 0.35
profit_2 = sum(data) - total_sales_2

print(abs(int(profit_2 - profit_1)), end=' ')
if profit_2 > profit_1:
    print(int(data[-1] * 0.65))
else:
    print(int(data[-1] * 0.60))
