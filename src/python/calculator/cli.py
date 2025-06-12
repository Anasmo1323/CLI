# src/python/calculator/cli.py
import argparse
import sys
from .calculator import Calculator

def main():
    """Main function for the command-line interface."""
    # Set up the main parser with a description and epilog for help text.
    parser = argparse.ArgumentParser(
        description="A robust hybrid Python/C command-line calculator.",
        epilog='Example: calc expr " -5.5 * 2 "'
    )
    # Use subparsers to handle different commands (like git's 'add', 'commit', etc.).
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # --- Command for 'op' mode ---
    # Perform a direct operation with two numbers.
    op_parser = subparsers.add_parser("op", help="Perform a direct operation with two numbers.")
    op_parser.add_argument("a", type=float, help="The first number (operand).")
    op_parser.add_argument("operation", choices=['+', '-', '*', '/'], help="The arithmetic operation to perform.")
    op_parser.add_argument("b", type=float, help="The second number (operand).")

    # --- Command for 'expr' mode ---
    # Evaluate a full string expression.
    expr_parser = subparsers.add_parser("expr", help="Evaluate a simple mathematical expression from a string.")
    expr_parser.add_argument("expression", type=str, help='The mathematical expression, e.g., "2.5 + 3.1".')

    args = parser.parse_args()

    try:
        result = None
        if args.command == 'op':
            # Map the operation string to the corresponding Calculator method.
            operations_map = {
                '+': Calculator.add,
                '-': Calculator.subtract,
                '*': Calculator.multiply,
                '/': Calculator.divide
            }
            result = operations_map[args.operation](args.a, args.b)
        elif args.command == 'expr':
            result = Calculator.calculate(args.expression)

        print(f"Result: {result}")

    # Catch expected errors and print a user-friendly message to stderr.
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    # Catch any other unexpected errors.
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
