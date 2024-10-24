def max_efficiency(arrivalTime):
    from collections import Counter
    
    # Count occurrences of each arrival time
    time_counts = Counter(arrivalTime)
    unique_times = sorted(time_counts.keys())
    n = len(unique_times)
    
    max_eff = float('-inf')
    
    for i in range(n):
        tests_count = 0
        for j in range(i, n):
            active_time = unique_times[j] - unique_times[i]
            tests_count += time_counts[unique_times[j]]
            
            if tests_count >= 2:
                efficiency = tests_count - active_time
                max_eff = max(max_eff, efficiency)
    
    return max_eff

# Example usage
arrivalTime = [6,6,6,6,6,6,6,7]
result = max_efficiency(arrivalTime)
print(f"Maximum efficiency: {result}")
