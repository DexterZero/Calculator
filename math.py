import math
import operator

# Supported operators mapped to functions
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

# Supported functions mapped to math module functions or custom
FUNCTIONS = {
    'sqrt': math.sqrt,
    'factorial': math.factorial,
    'log': math.log,          # natural log
    'log10': math.log10,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'degrees': math.degrees,
    'radians': math.radians,
}

def safe_eval(expr):
    """
    Safely evaluate a mathematical expression using Python's eval with limited globals.
    Supports math functions and operators.
    """
    allowed_names = {**FUNCTIONS, 'pi': math.pi, 'e': math.e}
    # Replace '^' with '**' for power operator
    expr = expr.replace('^', '**')

    try:
        # Evaluate expression with restricted globals and locals
        result = eval(expr, {"__builtins__": None}, allowed_names)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero."
    except (SyntaxError, NameError):
        return "Error: Invalid expression."
    except Exception as e:
        return f"Error: {e}"

def print_help():
    print("""
Supported operations:
- Basic arithmetic: +, -, *, /, ^
- Parentheses for grouping: ( )
- Functions: sqrt(x), factorial(x), log(x), log10(x), sin(x), cos(x), tan(x),
             asin(x), acos(x), atan(x), degrees(x), radians(x)
- Constants: pi, e

Examples:
  2 + 3 * 4
  sqrt(16)
  factorial(5)
  sin(pi / 2)
  log(10)
  2^8

Type 'exit' or 'quit' to leave the calculator.
""")

def main():
    print("Welcome to the Python Mathematical Calculator!")
    print_help()

    while True:
        expr = input("Enter expression: ").strip()
        if expr.lower() in ('exit', 'quit'):
            print("Goodbye!")
            break
        elif expr.lower() == 'help':
            print_help()
            continue
        elif not expr:
            continue

        result = safe_eval(expr)
        print("Result:", result)

if __name__ == "__main__":
    main()
