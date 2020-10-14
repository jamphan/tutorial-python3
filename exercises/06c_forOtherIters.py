FMT_HEADER = "="*80 + "\n" + "\t{:s}\n" + "="*80

print(FMT_HEADER.format("Simple range"))
for num in range(0,10):
    print(num)

print(FMT_HEADER.format("Even numbers"))
for even_nums in range(0,10,2):
    print(even_nums)

print(FMT_HEADER.format("Character strings"))
for char in "Hello, World!":
    print(char)

print(FMT_HEADER.format("List"))
for ele in ["a", 1, "b", 2, "c", 3]:
    print(ele)