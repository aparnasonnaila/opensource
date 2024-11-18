n = input().strip()
digit_sum = 0
for digit in n:
    digit_sum+=int(digit)
if digit_sum%2==0:
    print("Vignesh")
else:
    print("Charan")
