def generate_series(a):
    series = []
    for i in range(1, 2*a, 2):
        series.append(i)
    return series
a = int(input("Enter a number (a): "))
result = generate_series(a)
print("Output:", ", ".join(map(str, result)))
