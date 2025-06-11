#include "Multi.h"

PyObject* multiply(PyObject* self, PyObject* args) {
    double x, y;
    PyArg_ParseTuple(args, "dd", &x, &y);
    return Py_BuildValue("d", x * y);
}