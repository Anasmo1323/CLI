#include "Python.h"

#ifndef CLI_MODULE_ADD_H
#define CLI_MODULE_ADD_H

// Pure C function for internal use
double c_api_add(double a, double b);

// Python C-API wrapper function
PyObject* add(PyObject* self, PyObject* args);

#endif //CLI_MODULE_ADD_H