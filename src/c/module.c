#include <Python.h>
// Include the headers for all C modules that expose functions to Python.
#include "addition/add.h"
#include "subtraction/sub.h"
#include "multiplication/multi.h"
#include "division/div.h"
#include "ophandler/op_handler.h"

// Define the methods of this module that will be accessible from Python.
// Each entry is: {<python_name>, <c_function_name>, <argument_type>, <docstring>}
static PyMethodDef CalculatorMethods[] = {
    {"c_add", add, METH_VARARGS, "C function to add two numbers."},
    {"c_subtract", subtract, METH_VARARGS, "C function to subtract two numbers."},
    {"c_multiply", multiply, METH_VARARGS, "C function to multiply two numbers."},
    {"c_divide", divide, METH_VARARGS, "C function to divide two numbers."},
    {"c_calculate", operation_handler, METH_VARARGS, "C function to calculate a string expression like 'num1+num2'."},
    {NULL, NULL, 0, NULL} // Sentinel to mark the end of the method table.
};

// Define the module itself.
static struct PyModuleDef calculator_module = {
    PyModuleDef_HEAD_INIT,
    "calculator._c_calculator", // The name of the module (e.g., import calculator._c_calculator).
    "C backend for the calculator operations.", // Module docstring.
    -1, // Size of per-interpreter state of the module, or -1 if global.
    CalculatorMethods
};

// The module initialization function. This is called when Python imports the module.
// The function name MUST be PyInit_<module_name>.
PyMODINIT_FUNC PyInit__c_calculator(void) {
    return PyModule_Create(&calculator_module);
}
