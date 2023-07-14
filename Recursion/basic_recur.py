

count = 0

def recur(count):
    if count == 3:
        return
    print(count)
    count += 1
    recur(count)

recur(count)