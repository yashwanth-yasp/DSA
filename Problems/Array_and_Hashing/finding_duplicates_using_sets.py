
def find_duplicates(line):
    unordered_set = set(line)
    if len(unordered_set) < len(line):
        return True
    else:
        return False

line = list(map(int, input().split()))
print(find_duplicates(line))