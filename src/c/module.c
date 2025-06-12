#include <Python.h>
#include "addition/add.h"
#include "subtraction/sub.h"
#include "multiplication/multi.h"
#include "division/div.h"
#include "OpHandler/OpHandler.h"

static PyMethodDef CalculatorMethods[] = {
    {"c_add", add, METH_VARARGS, "Add two numbers"},
    {"c_subtract", subtract, METH_VARARGS, "Subtract two numbers"},
    {"c_multiply", multiply, METH_VARARGS, "Multiply two numbers"},
    {"c_divide", divide, METH_VARARGS, "Divide two numbers"},
    {"c_calculate", OperationHandler, METH_VARARGS, "Calculate expression"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef calculator_module = {
    PyModuleDef_HEAD_INIT,
    "_c_calculator",   // Module name
    "C backend for calculator operations",
    -1,
    CalculatorMethods
};

PyMODINIT_FUNC PyInit__c_calculator(void) {
    return PyModule_Create(&calculator_module);
}
