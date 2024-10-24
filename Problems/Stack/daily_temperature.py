
def temperature(temps):
    result = [0] * len(temps)
    stack = []

    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day
        stack.append(i)
    
    return result


line = [73,74,75,71,69,72,76,73]
print(temperature(line))

