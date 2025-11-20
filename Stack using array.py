stack=[1,2,3]
def push(x):
    stack.append(x)
def pop():
    return stack.pop()
def peep():
    return stack[-1]
def isempty():
    return len(stack)==0
print("Original stack is: ",stack)
print("Is Empty:",isempty())
print("Top element:",peep())
push(4)
print("Stack after push:",stack)
print("After pop:",pop())
print(stack)
