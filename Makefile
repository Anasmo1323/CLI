# Compiler and flags
CC = gcc
PYTHON_INCLUDES = $(shell python3-config --includes)
CFLAGS = -fPIC -shared $(PYTHON_INCLUDES)

# Source files
C_SRCS = $(wildcard src/c/*/*.c)
C_OBJS = $(C_SRCS:.c=.o)
TARGET = src/python/_c_calculator.so

# Python package
PACKAGE_DIR = src/python

.PHONY: all build test clean

all: build

build: $(TARGET)

$(TARGET): $(C_OBJS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

test:
	python -m pytest tests/

install:
	pip install .

clean:
	rm -f $(C_OBJS) $(TARGET)
	rm -rf build dist *.egg-info
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete