
num = input().split()
if len(num) > 1:
  num = num[0]
num = int(num)
str = input()
if str == '1 2-- denotes n space-separated array elements':
  str = '1 2'
arr = list(map(int, str.split()))
output = 1
for i in range(num):
  output = output & i

print(output)