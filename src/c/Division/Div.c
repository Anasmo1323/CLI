#include "div.h"
/**
 * Divides the first number by the second and returns a Python object.
 *
 * This C-Python API wrapper parses two float arguments from Python, calls
 * c_api_divide, and converts the result to a Python float object. It includes
 * a safeguard against division by zero.
 *
 * @param self Pointer to the module object (unused, required by C-Python API).
 * @param args Python tuple containing two numbers (as Python floats).
 * @return PyObject* A Python float object containing the result of a / b.
 *                   Returns NULL if argument parsing fails or if b is zero.
 */
PyObject* divide(PyObject* self, PyObject* args) {
    double x, y;
    if (!PyArg_ParseTuple(args, "dd", &x, &y)) {
        return NULL;
    }
    if (y == 0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "C-level check: division by zero");
        return NULL;
    }
    return Py_BuildValue("d", c_api_divide(x, y));
}

double c_api_divide(double a, double b) {
    return a / b;
}

