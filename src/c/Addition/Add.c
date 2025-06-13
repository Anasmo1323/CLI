#include "Add.h"
/**
 * Adds two numbers and returns a Python object containing the result.
 *
 * This function is a C-Python API wrapper that parses two float arguments from
 * Python, calls the core c_api_add function, and converts the result to a Python
 * float object.
 *
 * @param self Pointer to the module object (unused, required by C-Python API).
 * @param args Python tuple containing two numbers (as Python floats) to add.
 * @return PyObject* A Python float object containing the sum of the two numbers.
 *                   Returns NULL if argument parsing fails (e.g., non-float inputs).
 */
PyObject* add(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b))
        return NULL;
    
    double result = c_api_add(a, b);
    return Py_BuildValue("d", result);
}


double c_api_add(double a, double b) {
    return a + b;
}