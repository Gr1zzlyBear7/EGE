s = 250000
data = list(map(int, open('6')))
data.sort()
rare_books = list(filter(lambda x: x > 3000, data))
en_books = list(filter(lambda x: 2000 <= x <= 3000, data))
book = list(filter(lambda x: x < 2000, data))
new = [rare_books[0], rare_books[-1]]
for rare_book in rare_books:
    data.remove(rare_book)
for en_book in en_books:
    new.append(en_book)
    data.remove(en_book)
arr = []
s -= sum(new)
while sum(arr) + data[0] <= s:
    arr.append(data.pop(0))

for i in range(len(data)):
    if sum(arr) - arr[-1] + data[i] <= s:
        arr[-1], data[i] = data[i], arr[-1]
print(len(new + arr), arr[-1])
