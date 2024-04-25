import re
operators = {
    r'\+': 'Addition (+)', r'-': 'Subtraction (-)', r'\*': 'Multiplication (*)',
    r'/': 'Division (/)', r'==': 'Equal to (==)', r'<=': 'Less than or equalto (<=)'
}
input_str = input("Enter the expression: ")
for operator, description in operators.items():
    if re.search(operator, input_str):
        print("Operator:", description)
