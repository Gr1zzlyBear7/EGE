data = [x.split(' - ')[1] for x in open('3')]
with open('33', 'w') as f:
    for i in data:
        f.write(i)