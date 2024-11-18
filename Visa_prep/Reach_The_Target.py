T = int(input())
for _ in range(T):
    X, Y = map(int,input().split())
    winning_target = X+1
    runs_needed = winning_target - Y
    print(runs_needed)
