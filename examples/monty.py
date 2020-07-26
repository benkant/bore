## Whitespace Formatting

# The pound sign marks the start of a comment. Python itself
# ignores the comments, but they're helpful for anyone reading the code.
for i in [1, 2, 3, 4, 5]:
    print(i)  # first line in "for i" block
    for j in [1, 2, 3, 4, 5]:
        print(j)  # first line in "for j" block
        print(i + j)  # last line in "for j" block
    print(i)  # last line in "for i" block
print("done looping")
