s = open('zadacha-24-6ba07684-4454-436e-8147-5ba42fb16ef4.txt').readline()
# ans = []
# al = '0123456789'
# for x in range(ord('A'), ord('Z') + 1):
#     al += chr(x)
# for x in al:
#     for i in range(10000, -1, -1):
#         if x * i in s:
#             ans.append([x, i])
#             break
# ans.sort(key=lambda x: x[1])
# for x in ans:
#     print(x)
print(s.rfind('11111'))
print(s.rfind('22222'))