param([string]$Target = "build")

# Get the directory where the script is located and set it as PYTHONPATH
$env:PYTHONPATH = Split-Path -Parent $MyInvocation.MyCommand.Path

pytest tests/

# Temporarily allow script execution
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

# Run the build script
.\build.ps1 -Target $Target