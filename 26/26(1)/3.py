size = 524288
data = sorted(list(map(int, open('3.txt'))))
condition = size // 2
videos = list(filter(lambda x: x >= 101, data))
k = 0
for video in videos:
    if size <= condition:
        print(size, video)
        for photo in data:
            if size >= photo:
                k += 1
                size -= photo
        break
    else:
        size -= video
        k += 1

print(size, k)