# """Быстрое создание 20 питоновских файлов"""
# for i in range(1, 21):
#     with open(str(i) + '.py', mode='a') as f:
#         pass


with open('1.txt') as f:
    data = list(map(int, f.readlines()))
    ans = [num for num in data if num % 3 == 0 and
           num % 7 != 0 and num % 17 != 0 and num % 19 != 0 and num % 27 != 0]
    print(len(ans), max(ans))