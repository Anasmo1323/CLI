@echo off
setlocal enabledelayedexpansion

:: Configure paths
set BASE_DIR=%~dp0
set C_SRC_DIR=%BASE_DIR%src\c
set OUTPUT_DIR=%BASE_DIR%src\python\calculator

:: Compiler settings
set PYTHON_INCLUDES="C:\Users\Anas Mohamed\AppData\Local\Programs\Python\Python311\Include"
set GCC_CMD=gcc -shared -fPIC -I %PYTHON_INCLUDES% -o "%OUTPUT_DIR%\_c_calculator.pyd"

:: Source files
set C_FILES="%C_SRC_DIR%\addition\add.c" "%C_SRC_DIR%\subtraction\sub.c" "%C_SRC_DIR%\multiplication\multi.c" "%C_SRC_DIR%\division\div.c" "%C_SRC_DIR%\ophandler\op_handler.c" "%C_SRC_DIR%\module.c"

:: Build command
%GCC_CMD% %C_FILES%

echo Build complete! The C extension is at %OUTPUT_DIR%\_c_calculator.pyd