#include "OpHandler.h"
#include "../addition/add.h"
#include "../subtraction/sub.h"
#include "../multiplication/multi.h"
#include "../division/div.h"
#include <ctype.h>  // For isspace()

PyObject* OperationHandler(PyObject* self, PyObject* args) {
    const char *input;
    if (!PyArg_ParseTuple(args, "s", &input)) return NULL;

    // Remove whitespace
    char clean_input[256];
    int j = 0;
    for (int i = 0; input[i]; i++) {
        if (!isspace(input[i])) clean_input[j++] = input[i];
    }
    clean_input[j] = '\0';

    // Find operator position
    char* op_ptr = NULL;
    char operators[] = "+-*/";

    for (char* p = clean_input; *p; p++) {
        if (strchr(operators, *p) && p != clean_input) {
            op_ptr = p;
            break;
        }
    }

    if (!op_ptr) {
        PyErr_SetString(PyExc_ValueError, "No valid operator found");
        return NULL;
    }

    // Split into left and right parts
    char* end;
    double num1 = strtod(clean_input, &end);
    if (end != op_ptr) {
        PyErr_SetString(PyExc_ValueError, "Invalid first number");
        return NULL;
    }

    double num2 = strtod(op_ptr + 1, &end);
    if (*end != '\0') {
        PyErr_SetString(PyExc_ValueError, "Invalid second number");
        return NULL;
    }

    // Execute operation
    switch (*op_ptr) {
        case '+': return add(self, Py_BuildValue("(dd)", num1, num2));
        case '-': return subtract(self, Py_BuildValue("(dd)", num1, num2));
        case '*': return multiply(self, Py_BuildValue("(dd)", num1, num2));
        case '/':
            if (num2 == 0) {
                PyErr_SetString(PyExc_ZeroDivisionError, "Cannot divide by zero");
                return NULL;
            }
            return divide(self, Py_BuildValue("(dd)", num1, num2));
        default:
            PyErr_SetString(PyExc_ValueError, "Unsupported operation");
            return NULL;
    }
}