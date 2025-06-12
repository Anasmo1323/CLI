@echo off
setlocal enabledelayedexpansion

:: CLI tool for managing Python calculator project
:: Usage: cli.bat [command]

set "EXIT_CODE=0"

if "%1"=="build" (
    echo Building C extension...
    if exist build.bat (
        call build.bat
        if !ERRORLEVEL! neq 0 (
            echo Error: Build failed
            set "EXIT_CODE=1"
        )
    ) else (
        echo Error: build.bat not found
        set "EXIT_CODE=1"
    )
) else if "%1"=="test" (
    echo Running tests...
    where pytest >nul 2>&1
    if !ERRORLEVEL! neq 0 (
        echo Error: pytest not found. Please install it with: pip install pytest
        set "EXIT_CODE=1"
    ) else (
        pytest tests
        if !ERRORLEVEL! neq 0 (
            echo Error: Tests failed
            set "EXIT_CODE=1"
        )
    )
) else if "%1"=="install" (
    echo Installing package...
    where pip >nul 2>&1
    if !ERRORLEVEL! neq 0 (
        echo Error: pip not found
        set "EXIT_CODE=1"
    ) else (
        pip install .
        if !ERRORLEVEL! neq 0 (
            echo Error: Installation failed
            set "EXIT_CODE=1"
        )
    )
) else if "%1"=="clean" (
    echo Cleaning build artifacts...
    
    if exist "*.pyc" del /s /q "*.pyc"
    
    if exist "__pycache__" (
        rmdir /s /q "__pycache__"
    )
    
    if exist "src\python\calculator\_c_calculator.pyd" (
        del /q "src\python\calculator\_c_calculator.pyd"
    )
    
    for %%D in (build dist *.egg-info) do (
        if exist "%%D" rmdir /s /q "%%D"
    )
) else if "%1"=="-h" (
    goto :help
) else if "%1"=="--help" (
    goto :help
) else (
    :help
    echo Available commands:
    echo   build   - Compile C extension
    echo   test    - Run tests
    echo   install - Install package
    echo   clean   - Clean build artifacts
    echo   -h, --help - Show this help message
)

exit /b %EXIT_CODE%