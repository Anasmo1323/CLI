@echo off

if "%1"=="build" (
    call build.bat
) else if "%1"=="test" (
    pytest tests
) else if "%1"=="install" (
    pip install .
) else if "%1"=="clean" (
    del /s /q *.pyc
    rmdir /s /q __pycache__
    del /s /q src\python\calculator\_c_calculator.pyd
    rmdir /s /q build
    rmdir /s /q dist
    rmdir /s /q *.egg-info
) else (
    echo Available commands:
    echo   build   - Compile C extension
    echo   test    - Run tests
    echo   install - Install package
    echo   clean   - Clean build artifacts
)