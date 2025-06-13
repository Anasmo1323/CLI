#include "Multi.h"

/**
 * Multiplies two numbers and returns a Python object.
 *
 * This C-Python API wrapper parses two float arguments from Python, calls
 * c_api_multiply, and converts the result to a Python float object.
 *
 * @param self Pointer to the module object (unused, required by C-Python API).
 * @param args Python tuple containing two numbers (as Python floats).
 * @return PyObject* A Python float object containing the product of a and b.
 *                   Returns NULL if argument parsing fails.
 *
 */
PyObject* multiply(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    
    double result = c_api_multiply(a, b);
    return Py_BuildValue("d", result);
}


double c_api_multiply(double a, double b) {
    return a * b;
}