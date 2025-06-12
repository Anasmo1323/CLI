# Makefile for the Calculator project
# Acts as a high-level command runner for standard, professional workflows.

# --- Variables ---
CC := gcc
# CFLAGS for compiling the standalone C test runner.
# Note: The C extension is compiled by setuptools, which handles its own flags.
CFLAGS := -Wall -Wextra -std=c11 -fPIC
PYTHON := python3
PIP := pip3
PYTEST := pytest

# --- Directories and Files ---
TEST_DIR := tests
C_TEST_SRC := $(TEST_DIR)/test_c_operations.c
C_TEST_EXEC := $(TEST_DIR)/c_test_runner
# Core C source files needed to compile the standalone C test runner.
C_CORE_SOURCES := src/c/addition/add.c src/c/subtraction/sub.c src/c/multiplication/multi.c src/c/division/div.c

# --- Phony Targets (commands that don't produce a file with the same name) ---
.PHONY: all build install test clean test_c test_python

# The default target that runs when you just type 'make'.
all: build

# Builds the C extension and installs the package in editable mode.
# This correctly uses the Python packaging infrastructure (setuptools).
build:
	@echo "--> Building C extension and installing package in editable mode..."
	$(PIP) install --verbose -e .

# Convenience target. For an editable install, this is the same as 'build'.
install: build

# Run all C and Python tests.
test: test_c test_python

# Compiles and runs the C unit tests independently of Python, as required.
# This demonstrates the C core logic is testable on its own.
test_c: $(C_TEST_EXEC)
	@echo "\n--> Running Standalone C Unit Tests..."
	./$(C_TEST_EXEC)

# Rule to compile the C test runner executable.
$(C_TEST_EXEC): $(C_TEST_SRC) $(C_CORE_SOURCES)
	@echo "--> Compiling C test runner..."
	# We link with '-lm' for the math library (e.g., fabs).
	$(CC) $(CFLAGS) -o $@ $(C_TEST_SRC) $(C_CORE_SOURCES) -Isrc/c -lm

# Runs the Python tests using the standard pytest framework.
test_python:
	@echo "\n--> Running Python Unit Tests (via pytest)..."
	$(PYTEST) -v

# Cleans up all build artifacts, test executables, and cache files.
clean:
	@echo "--> Cleaning up build artifacts and cache files..."
	@rm -rf build/ dist/ *.egg-info/ .pytest_cache/
	@rm -f $(C_TEST_EXEC)
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.so" -delete
	@echo "Cleanup complete."

