
#adj_list input
vertices = int(input("Enter the no of vertices\n"))
print("Enter the adj list")
adj_list = {}
for i in range(vertices):
    line = list(map(int, input().split()))
    adj_list[line[0]] = line[1:]
visited = []
new_adj_list = [[i] for i in range(vertices)]



def dfs(i):
    for j in adj_list[i]:
        if j not in visited:
            new_adj_list[i].append(j)
            visited.append(j)
            dfs(j)


for i in range(vertices):
    dfs(i)
print(new_adj_list)