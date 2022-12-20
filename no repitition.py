stack = []

str = input()

for i in range(len(str)):
    if len(stack) == 0:
        stack.append(str[i])
    else:
        if stack[len(stack) - 1] == str[i]:
            stack.pop()
        else:
            stack.append(str[i])

finalString = ''

for item in stack:
    finalString += item
    
print(finalString)