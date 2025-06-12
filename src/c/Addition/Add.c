// In Add.c
#include "Add.h"

// Python wrapper function
PyObject* add(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    
    double result = c_api_add(a, b);
    return Py_BuildValue("d", result);
}

// Pure C function for direct C calls
double c_api_add(double a, double b) {
    return a + b;
}