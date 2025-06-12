// In your Sub.c file
#include "sub.h"

// Python wrapper function
PyObject* subtract(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    
    double result = c_api_subtract(a, b);
    return Py_BuildValue("d", result);
}

// Pure C function for direct C calls
double c_api_subtract(double a, double b) {
    return a - b;
}