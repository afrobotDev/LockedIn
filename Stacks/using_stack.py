from pop_and_peek import Stack 


def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if len(stack.items) == 0:
                return False
            stack.pop()
    
    return len(stack.items) == 0



 
