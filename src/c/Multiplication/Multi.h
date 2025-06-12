// In Multi.h
#ifndef CLI_MODULE_MULTI_H
#define CLI_MODULE_MULTI_H

#include "Python.h"

// Pure C function for internal use
double c_api_multiply(double a, double b);

// Python C-API wrapper function
PyObject* multiply(PyObject* self, PyObject* args);

#endif //CLI_MODULE_MULTI_H