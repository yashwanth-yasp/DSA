

str = input()

dic = {}
first = []
big = -99999999
for i in range(0, len(str), 2):
  if str[i] in dic:
    dic[str[i]] -= 1
  else: 
    dic[str[i]] = 1
  if dic[str[i]] > 0:
    first.append(str[i]) 
  elif dic[str[i]] > big: 
    first.remove(str[i])
    dic[str[i]] = big

for i in range(1, len(str), 2):
  if str[i] in dic:
    dic[str[i]] -= 1
  else: 
    dic[str[i]] = 1
  if dic[str[i]] > 0:
    first.append(str[i]) 
  elif dic[str[i]] > big: 
    first.remove(str[i])
    dic[str[i]] = big
  
if first:
  print(first[0])
else:
  print(-1)    
  