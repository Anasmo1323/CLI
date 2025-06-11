#include <Python.h>
#include "stdio.h"
#include "Addition/Add.h"
#include "Subtraction/Sub.h"
#include "Multiplication/Multi.h"
#include "Division/Div.h"
#include "OpHandler/OpHandler.h"


static PyMethodDef CLI_moduleMethods[] = {
        {"add", add, METH_VARARGS, "Add two numbers"},
        {"subtract", subtract, METH_VARARGS, "Subtract two numbers"},
        {"multiply", multiply, METH_VARARGS, "Multiply two numbers"},
        {"divide", divide, METH_VARARGS, "Divide two numbers"},
{"OperationHandler", OperationHandler, METH_VARARGS, "Handle an operation based on user input"},
        {NULL, NULL, 0, NULL}
};

static struct PyModuleDef CLI_module = {
        PyModuleDef_HEAD_INIT,
        "CLI_module",
        "Module for basic arithmetic operations",
        -1,
        CLI_moduleMethods
};

PyMODINIT_FUNC PyInit_CLI_module(void) {
    return PyModule_Create(&CLI_module);
}
//void main() {
//    const char version = "Anas";
//    printf((*version)[0]);
//}