import argparse
import sys
from .calculator import Calculator

def main():
    """Main function for the CLI tool."""
    parser = argparse.ArgumentParser(
        description="A hybrid Python/C command-line calculator.",
        epilog='Example: calc expr " -5.5 * 2 "'
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Command for evaluating a full string expression
    expr_parser = subparsers.add_parser("expr", help="Evaluate a simple mathematical expression from a string.")
    expr_parser.add_argument("expression", type=str, help='The mathematical expression to evaluate (e.g., "2.5+3.1").')

    # Command for direct operations
    op_parser = subparsers.add_parser("op", help="Perform a direct operation with two numbers.")
    op_parser.add_argument("a", type=float, help="The first number.")
    op_parser.add_argument("operation", choices=['+', '-', '*', '/'], help="The operation to perform.")
    op_parser.add_argument("b", type=float, help="The second number.")

    args = parser.parse_args()

    try:
        result = None
        if args.command == 'expr':
            result = Calculator.calculate(args.expression)
        elif args.command == 'op':
            operations = {
                '+': Calculator.add,
                '-': Calculator.subtract,
                '*': Calculator.multiply,
                '/': Calculator.divide
            }
            result = operations[args.operation](args.a, args.b)

        print(f"Result: {result}")

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()