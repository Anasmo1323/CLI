
#include "sub.h"

/**
 * Subtracts the second number from the first and returns a Python object.
 *
 * This C-Python API wrapper parses two float arguments from Python, calls
 * c_api_subtract, and converts the result to a Python float object.
 *
 * @param self Pointer to the module object (unused, required by C-Python API).
 * @param args Python tuple containing two numbers (as Python floats).
 * @return PyObject* A Python float object containing the result of a - b.
 *                   Returns NULL if argument parsing fails.
 *
 */
PyObject* subtract(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    
    double result = c_api_subtract(a, b);
    return Py_BuildValue("d", result);
}

double c_api_subtract(double a, double b) {
    return a - b;
}