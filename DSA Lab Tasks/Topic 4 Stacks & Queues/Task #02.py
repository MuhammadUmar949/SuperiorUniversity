# Postfix Expression Evaluation
def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 // operand2)
    return stack.pop()

# Test
expr = "5 1 2 + 4 * + 3 -"
print("Result:", evaluate_postfix(expr))  # Output: 14