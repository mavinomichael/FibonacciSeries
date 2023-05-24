from generate import Series

fibonacci = Series()

# non-efficient generator
print(fibonacci.generate_series(8))

# more efficient generator
generator = fibonacci.generate_efficiently(8)
for value in generator:
    print(value)
