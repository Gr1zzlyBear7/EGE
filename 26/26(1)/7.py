k = 100
m = 150
data = list(map(int, open('7')))
data.sort(reverse=True)
bigest_sales = data[:k]
data = data[k:]
sales = data[:m]
data = data[m:]
total_sale = 0
for sale in bigest_sales:
    total_sale += sale * 0.2
for sale in sales:
    total_sale += sale * 0.1
print(data[0], int(total_sale))