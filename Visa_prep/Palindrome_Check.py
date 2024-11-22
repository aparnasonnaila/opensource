n = int(input().strip())
matrix = []
for _ in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
for i in range(n):
    matrix[i] =matrix[i][::-1]
for row in matrix:
    print(" ".join(map(str, row)))
