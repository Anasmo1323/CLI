param([string]$Target = "build")
$ErrorActionPreference = "Stop"

# Check required tools
function Check-Requirements {
    try {
        $pythonVersion = python --version 2>&1
        Write-Host "Using $pythonVersion" -ForegroundColor Cyan
    } catch {
        throw "Python is not installed or not in PATH!"
    }

    # Check for gcc
    try {
        $gccVersion = gcc --version 2>&1
        Write-Host "Using gcc: $($gccVersion[0])" -ForegroundColor Cyan
    } catch {
        throw "GCC is not installed or not in PATH!"
    }

    # Check for required Python packages
    if ($Target.ToLower() -eq "test") {
        try {
            python -c "import pytest" 2>$null
        } catch {
            throw "pytest is not installed. Please run: pip install pytest"
        }
    }
}

function Build-CExtension {
    Write-Host "Building C extension using distutils..." -ForegroundColor Cyan

    # Create temporary setup file
    $setupContent = @"
from setuptools import setup, Extension
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

extension = Extension(
    'calculator._c_calculator',
    sources=[
        os.path.join(base_dir, 'src', 'c', 'addition', 'add.c'),
        os.path.join(base_dir, 'src', 'c', 'subtraction', 'sub.c'),
        os.path.join(base_dir, 'src', 'c', 'multiplication', 'multi.c'),
        os.path.join(base_dir, 'src', 'c', 'division', 'div.c'),
        os.path.join(base_dir, 'src', 'c', 'OpHandler', 'op_handler.c'),
        os.path.join(base_dir, 'src', 'c', 'module.c')
    ],
    include_dirs=[os.path.join(base_dir, 'src', 'c')]
)

setup(
    name='c_extension_builder',
    version='0.1',
    ext_modules=[extension],
)
"@
    Set-Content -Path "setup_extension.py" -Value $setupContent

    # Build using Python's build system
    python setup_extension.py build_ext --inplace

    # Move the built file to the correct location
    $builtFile = Get-ChildItem -Path "build" -Recurse -Filter "_c_calculator*.pyd" | Select-Object -First 1
    if ($builtFile) {
        $dest = "src/python/calculator/_c_calculator.pyd"
        Move-Item -Path $builtFile.FullName -Destination $dest -Force
        Write-Host "C extension built and moved to $dest" -ForegroundColor Green
    } else {
        throw "Failed to build C extension using distutils"
    }

    # Cleanup
    Remove-Item -Recurse -Force build
    Remove-Item setup_extension.py
}
function Run-Tests {
    Write-Host "Running tests..." -ForegroundColor Cyan
    try {
        pytest tests
        if ($LASTEXITCODE -ne 0) {
            throw "Tests failed with exit code $LASTEXITCODE"
        }
    } catch {
        throw "Test execution failed: $_"
    }
    Write-Host "Tests completed successfully!" -ForegroundColor Green
}

function Install-Package {
    Write-Host "Installing package..." -ForegroundColor Cyan
    try {
        pip install .
        if ($LASTEXITCODE -ne 0) {
            throw "Package installation failed with exit code $LASTEXITCODE"
        }
    } catch {
        throw "Package installation failed: $_"
    }
    Write-Host "Package installed successfully!" -ForegroundColor Green
}

function Clean-Build {
    Write-Host "Cleaning build artifacts..." -ForegroundColor Cyan
    # Remove compiled files
    Get-ChildItem -Recurse -Include *.pyc, *.pyd, *.o, *.so | Remove-Item -Force -ErrorAction SilentlyContinue
    # Remove build directories
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue build, dist, *.egg-info
    # Remove Python cache
    Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "Clean completed!" -ForegroundColor Green
}

# Main execution
try {
    Check-Requirements

    switch ($Target.ToLower()) {
        "build"   { Build-CExtension }
        "test"    {
            Build-CExtension  # Build before testing
            Run-Tests
        }
        "install" {
            Build-CExtension  # Build before installing
            Install-Package
        }
        "clean"   { Clean-Build }
        default {
            Write-Host "Available targets:" -ForegroundColor Yellow
            Write-Host "  build   - Compile C extension"
            Write-Host "  test    - Run tests (builds first)"
            Write-Host "  install - Install package (builds first)"
            Write-Host "  clean   - Clean build artifacts"
        }
    }
} catch {
    Write-Host "ERROR: $_" -ForegroundColor Red
    exit 1
}