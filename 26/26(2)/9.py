data = [list(map(int, x.split())) for x in open('9')]
years = set([x[0] for x in data])
my_years = {}
for year in years:
    my_years[year] = set()
for year, mark in data:
    my_years[year].add(mark)
total = 0
for year in my_years:
    total += 8 - len(my_years[year])
sigma_arr = sorted(my_years.items(), key=lambda x: (len(x[1]), -x[0]))
for year in sigma_arr:
    print(total, year)
    break