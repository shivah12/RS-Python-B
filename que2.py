digits = [4,3,2,1]
digits_1st = []
for i in digits:
    digits_1st.append(str(i))
a = ["r","o","b","o"]
digits_1st = "".join(digits_1st)
digits_1st = int(digits_1st)
print(digits_1st+1)
digits = list(str(digits_1st+1))
result = []
for digit in digits:
    result.append(int(digit))
print(result)