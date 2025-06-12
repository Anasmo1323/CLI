// In your sub.h file
#ifndef CLI_MODULE_SUB_H
#define CLI_MODULE_SUB_H
#define PY_SSIZE_T_CLEAN
#include <Python.h>


PyObject* subtract(PyObject* self, PyObject* args);  // Python wrapper
double c_api_subtract(double a, double b);           // C API function

#endif //CLI_MODULE_SUB_H