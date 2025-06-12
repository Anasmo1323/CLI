#include "div.h"

// Pure C logic, callable from other C files
double c_api_divide(double a, double b) {
    return a / b;
}

// Wrapper exposed to Python
PyObject* divide(PyObject* self, PyObject* args) {
    double x, y;
    if (!PyArg_ParseTuple(args, "dd", &x, &y)) {
        return NULL;
    }
    if (y == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "C-level check: division by zero");
        return NULL;
    }
    return Py_BuildValue("d", c_api_divide(x, y));
}