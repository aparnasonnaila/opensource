T = int(input().strip())
for _ in range(T):
    try:
        x,n=map(int,input().split())
        points_test_case=x//10
        score=points_test_case*n
        print(score)
    except ValueError:
        print("Invalid Test Case")
