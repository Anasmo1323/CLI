#include "op_handler.h"
#include "../addition/add.h"
#include "../subtraction/sub.h"
#include "../multiplication/multi.h"
#include "../division/div.h"
#include <string.h> // For strchr, strlen
#include <stdlib.h> // For strtod
#include <ctype.h>  // For isspace

PyObject* operation_handler(PyObject* self, PyObject* args) {
    const char *input_str;
    if (!PyArg_ParseTuple(args, "s", &input_str)) {
        return NULL;
    }

    // Create a mutable copy of the input to remove whitespace
    char* clean_input = (char*)malloc(strlen(input_str) + 1);
    if (!clean_input) {
        return PyErr_NoMemory();
    }
    int j = 0;
    for (int i = 0; input_str[i]; i++) {
        if (!isspace((unsigned char)input_str[i])) {
            clean_input[j++] = input_str[i];
        }
    }
    clean_input[j] = '\0';

    char* op_ptr = NULL;
    // Find the first operator after the first character
    for (char* p = clean_input + 1; *p; p++) {
        if (strchr("+-*/", *p)) {
            op_ptr = p;
            break;
        }
    }

    if (!op_ptr) {
        PyErr_SetString(PyExc_ValueError, "Invalid expression: operator not found or is at the start.");
        free(clean_input);
        return NULL;
    }

    char* end_num1;
    char* end_num2;
    double num1 = strtod(clean_input, &end_num1);
    double num2 = strtod(op_ptr + 1, &end_num2);

    // Validate parsing
    if (end_num1 != op_ptr || *end_num2 != '\0') {
        PyErr_SetString(PyExc_ValueError, "Invalid number format in expression.");
        free(clean_input);
        return NULL;
    }

    free(clean_input);

    double result;
    switch (*op_ptr) {
        case '+':
            result = c_api_add(num1, num2);
            break;
        case '-':
            result = c_api_subtract(num1, num2);
            break;
        case '*':
            result = c_api_multiply(num1, num2);
            break;
        case '/':
            if (num2 == 0) {
                PyErr_SetString(PyExc_ZeroDivisionError, "Cannot divide by zero.");
                return NULL;
            }
            result = c_api_divide(num1, num2);
            break;
        default:
            PyErr_SetString(PyExc_ValueError, "Unsupported operation.");
            return NULL;
    }

    return Py_BuildValue("d", result);
}