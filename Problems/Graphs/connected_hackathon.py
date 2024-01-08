
num = int(input())
lines = []
for i in range(num - 1):
    line = list(map(int, input().split()))
    lines.append(line)

matrix = [[0]*num]*num
print(matrix)

print(lines)
for i in lines:
    print(i)
    matrix[i[0] - 1][i[1] - 1] = i[2],i[3]
    print(matrix)

