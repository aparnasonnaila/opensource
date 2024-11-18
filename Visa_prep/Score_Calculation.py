T = int(input())
for _ in range(T):
    X, N = map(int,input().split())
    points_per_test_case = X // 10
    score = N*points_per_test_case
    print(score)
