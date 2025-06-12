// In Multi.c
#include "Multi.h"

// Python wrapper function
PyObject* multiply(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    
    double result = c_api_multiply(a, b);
    return Py_BuildValue("d", result);
}

// Pure C function for direct C calls
double c_api_multiply(double a, double b) {
    return a * b;
}