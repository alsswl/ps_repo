N = int(input())
time = list(map(int, input().split()))
time = sorted(time)

cum_time = [time[0]]

for i in range(1, N):
    cum_time.append(cum_time[i-1]+time[i])

print(sum(cum_time))
