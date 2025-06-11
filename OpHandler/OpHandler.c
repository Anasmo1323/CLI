#include "OpHandler.h"
#include <string.h>
#include <stdlib.h>
#include "../Addition/Add.h"
#include "../Subtraction/Sub.h"
#include "../Multiplication/Multi.h"
#include "../Division/Div.h"

PyObject* OperationHandler(PyObject* self, PyObject* args) {
    const char *op;
PyArg_ParseTuple(args, "s", &op);

char operations[4] = {'+', '-', '*', '/'};

for (int i = 0; i < 4; i++) {
    if (strchr(op, operations[i]) != NULL)
    {
        char *operation_pos = strchr(op, operations[i]);
        char *end = strchr(op, '\0');

        double num1 = strtod(op, &operation_pos);

        operation_pos++;

        double num2 = strtod(operation_pos, &end);

        switch (operations[i]) {
            case '+':
                return add(self, Py_BuildValue("(dd)", num1, num2));
            case '-':
                return subtract(self, Py_BuildValue("(dd)", num1, num2));
            case '*':
                return multiply(self, Py_BuildValue("(dd)", num1, num2));
            case '/':
                if (num2 == 0) {
                    PyErr_SetString(PyExc_ZeroDivisionError, "Division by zero is not allowed");
                    return NULL;
                }
                return divide(self, Py_BuildValue("(dd)", num1, num2));

            default:
                return Py_BuildValue("s", "Unknown operation");
        }
    }
}

}
