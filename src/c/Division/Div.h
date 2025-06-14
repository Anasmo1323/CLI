
#ifndef CLI_MODULE_DIV_H
#define CLI_MODULE_DIV_H
#define PY_SSIZE_T_CLEAN
#include <Python.h>
// Pure C function for internal use
double c_api_divide(double a, double b);

// Python C-API wrapper function
PyObject* divide(PyObject* self, PyObject* args);

#endif //CLI_MODULE_DIV_H