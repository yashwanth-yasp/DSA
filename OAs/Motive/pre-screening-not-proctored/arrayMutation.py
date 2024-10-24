def mutate_array(a):
    n = len(a)
    b = [0] * n 
    
    for i in range(n):
        prev = a[i - 1] if i - 1 >= 0 else 0  
        curr = a[i]                           
        next = a[i + 1] if i + 1 < n else 0   
        
        b[i] = prev + curr + next
    
    return b

a = [4, 0, 1, -2, 3]
print(mutate_array(a))  