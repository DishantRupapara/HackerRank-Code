def strangeCounter(t):
    start = 3
    cycle_start_time = 1
    
    while t > cycle_start_time + start - 1:
        cycle_start_time += start
        start *= 2
    
    return start - (t - cycle_start_time)

# Input
t = int(input())
print(strangeCounter(t))
