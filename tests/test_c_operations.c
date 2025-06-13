#include <assert.h>
#include <stdio.h>
#include <math.h> // For fabs()

// Include the C headers for the core logic functions we are testing.
// We are testing the `c_api_*` functions directly, NOT the Python wrappers.
#include "../src/c/addition/add.h"
#include "../src/c/subtraction/sub.h"
#include "../src/c/multiplication/multi.h"
#include "../src/c/division/div.h"

// Define a small tolerance for comparing floating-point numbers.
#define TOLERANCE 1e-9

void test_c_api_add() {
    printf("Testing c_api_add... ");
    assert(fabs(c_api_add(1.0, 2.0) - 3.0) < TOLERANCE);
    assert(fabs(c_api_add(-1.0, 1.0) - 0.0) < TOLERANCE);
    assert(fabs(c_api_add(0.0, 0.0) - 0.0) < TOLERANCE);
    assert(fabs(c_api_add(1.23, 4.56) - 5.79) < TOLERANCE);
    printf("PASSED\n");
}

void test_c_api_subtract() {
    printf("Testing c_api_subtract... ");
    assert(fabs(c_api_subtract(5.0, 2.0) - 3.0) < TOLERANCE);
    assert(fabs(c_api_subtract(2.0, 5.0) - -3.0) < TOLERANCE);
    assert(fabs(c_api_subtract(-5.0, -2.0) - -3.0) < TOLERANCE);
    printf("PASSED\n");
}

void test_c_api_multiply() {
    printf("Testing c_api_multiply... ");
    assert(fabs(c_api_multiply(3.0, 4.0) - 12.0) < TOLERANCE);
    assert(fabs(c_api_multiply(-3.0, 4.0) - -12.0) < TOLERANCE);
    assert(fabs(c_api_multiply(3.0, 0.0) - 0.0) < TOLERANCE);
    printf("PASSED\n");
}

void test_c_api_divide() {
    printf("Testing c_api_divide... ");
    assert(fabs(c_api_divide(10.0, 2.0) - 5.0) < TOLERANCE);
    assert(fabs(c_api_divide(-10.0, 2.0) - -5.0) < TOLERANCE);
    // Note: The standalone C test doesn't check for division by zero,
    // as that involves setting a Python-specific exception.
    // That behavior is tested via the Python tests.
    printf("PASSED\n");
}

// Main function to run all the C unit tests.
int main() {
    printf("--- Running Standalone C Core Logic Tests ---\n");
    test_c_api_add();
    test_c_api_subtract();
    test_c_api_multiply();
    test_c_api_divide();
    printf("--- All C Tests Passed Successfully ---\n");
    return 0;
}
