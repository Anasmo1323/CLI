# Makefile for Unix/Linux systems
# This provides a convenient interface for building, testing, and managing the project

# Configuration
PYTHON := python3
PIP := pip3
C_COMPILER := gcc
C_TEST_EXECUTABLE := test_c_operations

# Directories
SRC_C_DIR := src/c
SRC_PYTHON_DIR := src/python
TESTS_DIR := tests
BUILD_DIR := build

# Source files for C extension
C_SOURCES := $(SRC_C_DIR)/module.c \
             $(SRC_C_DIR)/addition/add.c \
             $(SRC_C_DIR)/subtraction/sub.c \
             $(SRC_C_DIR)/multiplication/multi.c \
             $(SRC_C_DIR)/division/div.c \
             $(SRC_C_DIR)/ophandler/op_handler.c

# Test source for standalone C tests
C_TEST_SOURCE := $(TESTS_DIR)/test_c_operations.c

# Default target
.PHONY: all
all: build

# Build the Python package with C extension
.PHONY: build
build:
	@echo "Building Python package with C extension..."
	$(PYTHON) setup.py build_ext --inplace
	@echo "Build complete!"

# Install the package in development mode
.PHONY: install
install:
	@echo "Installing package in development mode..."
	$(PIP) install -e .
	@echo "Installation complete!"

# Install the package normally
.PHONY: install-prod
install-prod:
	@echo "Installing package..."
	$(PIP) install .
	@echo "Installation complete!"

# Run Python tests
.PHONY: test
test:
	@echo "Running Python tests..."
	$(PYTHON) -m pytest $(TESTS_DIR)/test_python.py -v
	@echo "Python tests complete!"

# Build and run standalone C tests
.PHONY: test-c
test-c: $(C_TEST_EXECUTABLE)
	@echo "Running standalone C tests..."
	./$(C_TEST_EXECUTABLE)
	@echo "C tests complete!"

# Compile standalone C test executable
$(C_TEST_EXECUTABLE): $(C_TEST_SOURCE) $(C_SOURCES)
	@echo "Compiling C test executable..."
	$(C_COMPILER) -o $(C_TEST_EXECUTABLE) $(C_TEST_SOURCE) \
		$(SRC_C_DIR)/addition/add.c \
		$(SRC_C_DIR)/subtraction/sub.c \
		$(SRC_C_DIR)/multiplication/multi.c \
		$(SRC_C_DIR)/division/div.c \
		$(SRC_C_DIR)/ophandler/op_handler.c \
		-I$(SRC_C_DIR) -lm
	@echo "C test executable compiled!"

# Run all tests (Python and C)
.PHONY: test-all
test-all: test test-c
	@echo "All tests completed!"

# Clean build artifacts
.PHONY: clean
clean:
	@echo "Cleaning build artifacts..."
	rm -rf $(BUILD_DIR)
	rm -rf dist
	rm -rf *.egg-info
	rm -rf $(SRC_PYTHON_DIR)/calculator/*.so
	rm -rf $(SRC_PYTHON_DIR)/calculator/_c_calculator*.so
	rm -f $(C_TEST_EXECUTABLE)
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "Clean complete!"

# Install development dependencies
.PHONY: install-dev
install-dev:
	@echo "Installing development dependencies..."
	$(PIP) install -r requirements.txt
	$(PIP) install -e .[dev]
	@echo "Development dependencies installed!"

# Format code (if black is available)
.PHONY: format
format:
	@echo "Formatting Python code..."
	black $(SRC_PYTHON_DIR) $(TESTS_DIR) --line-length 88
	@echo "Code formatting complete!"

# Lint code (if flake8 is available)
.PHONY: lint
lint:
	@echo "Linting Python code..."
	flake8 $(SRC_PYTHON_DIR) $(TESTS_DIR) --max-line-length 88
	@echo "Code linting complete!"

# Create a distributable package
.PHONY: dist
dist: clean
	@echo "Creating distribution packages..."
	$(PYTHON) setup.py sdist bdist_wheel
	@echo "Distribution packages created in dist/"

# Show help
.PHONY: help
help:
	@echo "Available make targets:"
	@echo "  build        - Build the Python package with C extension"
	@echo "  install      - Install package in development mode"
	@echo "  install-prod - Install package normally"
	@echo "  test         - Run Python tests"
	@echo "  test-c       - Build and run standalone C tests"
	@echo "  test-all     - Run both Python and C tests"
	@echo "  clean        - Clean build artifacts"
	@echo "  install-dev  - Install development dependencies"
	@echo "  format       - Format code with black"
	@echo "  lint         - Lint code with flake8"
	@echo "  dist         - Create distributable packages"
	@echo "  help         - Show this help message"