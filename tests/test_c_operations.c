#include <assert.h>
#include <stdio.h>
#include <math.h> // For fabs

#include "../src/c/addition/add.h"
#include "../src/c/subtraction/sub.h"
#include "../src/c/multiplication/multi.h"
#include "../src/c/division/div.h"

// Define a small tolerance for floating point comparisons
#define TOLERANCE 1e-9

void test_addition() {
    printf("Testing C add...\n");
    assert(fabs(c_api_add(1.0, 2.0) - 3.0) < TOLERANCE);
    assert(fabs(c_api_add(-1.0, 1.0) - 0.0) < TOLERANCE);
    assert(fabs(c_api_add(0.0, 0.0) - 0.0) < TOLERANCE);
    printf("OK\n");
}

void test_subtraction() {
    printf("Testing C subtract...\n");
    assert(fabs(c_api_subtract(5.0, 2.0) - 3.0) < TOLERANCE);
    assert(fabs(c_api_subtract(2.0, 5.0) - -3.0) < TOLERANCE);
    printf("OK\n");
}

void test_multiplication() {
    printf("Testing C multiply...\n");
    assert(fabs(c_api_multiply(3.0, 4.0) - 12.0) < TOLERANCE);
    assert(fabs(c_api_multiply(-3.0, 4.0) - -12.0) < TOLERANCE);
    assert(fabs(c_api_multiply(3.0, 0.0) - 0.0) < TOLERANCE);
    printf("OK\n");
}

void test_division() {
    printf("Testing C divide...\n");
    assert(fabs(c_api_divide(10.0, 2.0) - 5.0) < TOLERANCE);
    assert(fabs(c_api_divide(-10.0, 2.0) - -5.0) < TOLERANCE);
    printf("OK\n");
}

int main() {
    printf("--- Running C Unit Tests ---\n");
    test_addition();
    test_subtraction();
    test_multiplication();
    test_division();
    printf("--- All C Tests Passed ---\n");
    return 0;
}