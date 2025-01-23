s = 500
data = [list(map(int, x.split())) for x in open('13')]
articles = list(set([x[0] for x in data]))
articles.sort()
my_articles = {}
for article in articles:
    my_articles[article] = [[], 0]
for article, weight in data:
    my_articles[article][0].append(weight)
for article in my_articles:
    my_articles[article][0].sort()
total = 0
maxis = []
for article in my_articles:
    arr = my_articles[article][0]
    weights = []
    while sum(weights) + arr[0] <= s:
        weights.append(arr.pop(0))
        if len(arr) == 0:
            break
    my_articles[article][1] += (len(arr))
    total += len(arr)
    maxis.append(sum(arr))
ind = maxis.index(max(maxis))
k = 0
for article in my_articles:
    if k == ind:
        print(total, article)
        break
    k += 1