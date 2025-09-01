def generate_series(a):
    b = a if a % 2 != 0 else a - 1
    series = []
    for i in range(1, 2*b, 2):
        series.append(i)
    return series
a = int(input("Enter a number (a): "))
result = generate_series(a)
print("Output:", ", ".join(map(str, result)))
