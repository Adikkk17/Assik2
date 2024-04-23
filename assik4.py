def reverse_stack(stack):
    if len(stack) == 0:
        return
    item = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, item)

def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)
stack_input = input().split()
stack = [int(x) for x in stack_input]
reverse_stack(stack)
print(stack)
