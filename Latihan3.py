#menampilkan output * berbentuk diamond
inputData = eval(unput("Enter diamond's height: "))

for i in range(inputData):
    print(" " * (inputData - i), "*" * (2*i + 1))
for i in range(inputData - 2, -1, -1):
    print(" " * (inputData - i), "*" * (2*i + 1))
 