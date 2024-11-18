A,B,C,D = map(int,input().split())
if A+B>=D or A+C>=D or B+C>=D:
    print("YES")
else:
    print("NO")
